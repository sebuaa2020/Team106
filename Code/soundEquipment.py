import os
import time
class soundEquipment:
    def start(self):
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_simple.launch; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"roslaunch voice_ctrl my_voice_cmd.launch; exec bash\"'")
    def play(self):  #可以显示识别的关键词
        os.system("gnome-terminal -e 'bash -c \"roslaunch voice_ctrl my_voice_cmd.launch; exec bash\"'")
        
    def getText(self):  #获得self.text的值，作为后续确认
        #return self.text  
        pass
