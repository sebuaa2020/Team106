#include <ros/ros.h>
#include <std_msgs/String.h>
#include <geometry_msgs/Twist.h>

#define CMD_STOP        0
#define CMD_FORWARD     1
#define CMD_BACKWARD    2  
#define CMD_LEFT        3
#define CMD_RIGHT       4   

#define CMD_DURATION    300

static ros::Publisher vel_pub;
static ros::Publisher spk_pub;
static int nCmd = CMD_STOP;
static int nCount = 0;

void control_vel(const std_msgs::String::ConstPtr & msg)
{
    int find=0;
    bool bCmd=false;
    find=msg->data.find("导航");
    if(find>=0){
        bCmd=true;
        nCmd=1;
    }
    find = msg->data.find("前");
    if( find >= 0 )
    {
        bCmd = true;
        nCmd = CMD_FORWARD;
    }
    find = msg->data.find("后");
    if( find >= 0 )
    {
        bCmd = true;
        nCmd = CMD_BACKWARD;
    }
    find = msg->data.find("左");
    if( find >= 0 )
    {
        bCmd = true;
        nCmd = CMD_LEFT;
    }

    find = msg->data.find("右");
    if( find >= 0 )
    {
        bCmd = true;
        nCmd = CMD_RIGHT;
    }

    find = msg->data.find("停");
    if( find >= 0 )
    {
        bCmd = true;
        nCmd = CMD_STOP;
    }
    //正确指令bcmd=true
    if(bCmd==true){
        nCount=CMD_DURATION;
        std_msgs::String strGet;
        strGet.data="收到";
        spk_pub.publish(strGet);
    }
    else{
        std_msgs::String strWrg;
        strWrg.data="抱歉请再说一次";
        spk_pub.publish(strWrg);
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "my_voice_cmd");

    ros::NodeHandle n;
    ros::Subscriber sub_sr = n.subscribe("voiceWords", 10, control_vel);
    spk_pub = n.advertise<std_msgs::String>("tts", 20);
    vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);

    //开启
    sleep(1);
    std_msgs::String strBegin;
    strBegin.data="语音控制开启";
    spk_pub.publish(strBegin);

    ros::Rate r(10);
    while(ros::ok())
    {
        geometry_msgs::Twist vel_cmd;
        
        if(nCount > 0)
        {
            nCount --;
            if(nCmd == CMD_FORWARD)
            {
                vel_cmd.linear.x = 0.1;
                //ROS_WARN("forward");
            }
            if(nCmd == CMD_BACKWARD)
            {
                vel_cmd.linear.x = -0.1;
                //ROS_WARN("backward");
            }
            if(nCmd == CMD_LEFT)
            {
                vel_cmd.angular.z = 0.1;
                //ROS_WARN("left");
            }
            if(nCmd == CMD_RIGHT)
            {
                vel_cmd.angular.z = -0.1;
                //ROS_WARN("right");
            }
            if(nCmd == CMD_STOP)
            {
                vel_cmd.linear.x = 0;
                vel_cmd.linear.y = 0;
                vel_cmd.angular.z = 0;
                //ROS_WARN("stop");
            }
        }
        else
        {
            nCmd = CMD_STOP;
            vel_cmd.linear.x = 0;
            vel_cmd.linear.y = 0;
            vel_cmd.angular.z = 0;
            //ROS_WARN("stop");
        }
        vel_pub.publish(vel_cmd);
        ros::spinOnce();
        r.sleep();
    }

    return 0;
}