#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "qisr.h"
#include "msp_cmn.h"
#include "msp_errors.h"
#include "speech_recognizer.h"
#include <iconv.h>
 
#include "ros/ros.h"
#include "std_msgs/String.h"
 
#define FRAME_LEN   640 
#define BUFFER_SIZE 4096
 
int wakeupFlag   = 1 ;
int resultFlag   = 0 ;
 
static void show_result(char *string, char is_over)
{
    resultFlag=1;   
    printf("\rResult: [ %s ]", string);
    if(is_over)
        putchar('\n');
}
 
static char *g_result = NULL;

static unsigned int g_buffersize = BUFFER_SIZE;
 
void on_result(const char *result, char is_last)
{
    if (result) {
        size_t left = g_buffersize - 1 - strlen(g_result);
        size_t size = strlen(result);
        if (left < size) {
            g_result = (char*)realloc(g_result, g_buffersize + BUFFER_SIZE);
            if (g_result)
                g_buffersize += BUFFER_SIZE;
            else {
                printf("mem alloc failed\n");
                return;
            }
        }
        strncat(g_result, result, size);
        show_result(g_result, is_last);
    }
}
 

void on_speech_begin()
{
    if (g_result)
    {
        free(g_result);
    }
    g_result = (char*)malloc(BUFFER_SIZE);
    g_buffersize = BUFFER_SIZE;
    memset(g_result, 0, g_buffersize);
 
    printf("Start Listening...\n");
}
void on_speech_end(int reason)
{
    if (reason == END_REASON_VAD_DETECT)
        printf("\nSpeaking done \n");
    else
        printf("\nRecognizer error %d\n", reason);
}
 


//语音识别demo
static void demo_mic(const char* session_begin_params)
{
    int errcode;
    int i = 0;
 
    struct speech_rec iat;
 
    struct speech_rec_notifier recnotifier = {
        on_result,
        on_speech_begin,
        on_speech_end
    };
 
    errcode = sr_init(&iat, session_begin_params, SR_MIC, &recnotifier);
    if (errcode) {
        printf("speech recognizer init failed\n");
        return;
    }
    errcode = sr_start_listening(&iat);
    if (errcode) {
        printf("start listen failed %d\n", errcode);
    }
    //录音时间
    while(i++ < 3)
        sleep(1);
    errcode = sr_stop_listening(&iat);
    if (errcode) {
        printf("stop listening failed %d\n", errcode);
    }
 
    sr_uninit(&iat);
}


int main(int argc, char* argv[])
{
    // 初始化ROS
    ros::init(argc, argv, "voiceRecognition");
    ros::NodeHandle n;
    ros::Rate loop_rate(10);
 
    // 发布识别到的文本  
    ros::Publisher voiceWordsPub = n.advertise<std_msgs::String>("voiceWords", 1000);
 
    ROS_INFO("Sleeping...");
    int count=0;
    int once=1;

    while(ros::ok())
    {
        if (wakeupFlag){
            ROS_INFO("Wakeup...");
            int ret = MSP_SUCCESS;
            const char* login_params = "appid = 58eeeedf, work_dir = .";
 
            const char* session_begin_params =
                "sub = iat, domain = iat, language = zh_cn, "
                "accent = mandarin, sample_rate = 16000, "
                "result_type = plain, result_encoding = utf8";
 
            ret = MSPLogin(NULL, NULL, login_params);
            if(MSP_SUCCESS != ret){
                MSPLogout();
                printf("MSPLogin failed , Error code %d.\n",ret);
            }
 
            printf("Demo recognizing the speech from microphone\n");
	
	        printf("Speak in 3 seconds\n");
            //首次播报时间
            if(once==1){
                sleep(3);
                once--;
            }
 	
            demo_mic(session_begin_params);
 
            printf("3 sec passed\n");
        
            wakeupFlag=1;
            MSPLogout();
        }
 
        // 语音识别完成
        if(resultFlag)
	    {
            resultFlag=0;
            std_msgs::String msg;
            msg.data = g_result;
            voiceWordsPub.publish(msg);
            //留出时间进行播报
            sleep(3);
        }
 
        ros::spinOnce();
        loop_rate.sleep();
        count++;
    }
 
exit:
    MSPLogout(); // Logout...
 
    return 0;
}