import os
import time
from PIL import Image
#将地图保存到demo2_ws/src/wpr_simulation/下
class slamMap:
    def buildMap(self):  #开启slam建图
        return
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_simple.launch; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials hector_mapping.launch; exec bash\"'")#打开slam建图
        #time.sleep(2)
        #os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation keyboard_vel_ctrl; exec bash\"'")
        
    def saveMap(self):  #保存建好的图，并且把它复制到相应的地方
        return
        os.system("gnome-terminal -e 'bash -c \"rosrun map_server map_saver -f map; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/demo2_ws/src/wpr_simulation/maps/\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/demo2_ws/src/wpr_simulation/maps/\"'")
    def getMap(self):
        path=' ~/demo2_ws/src/wpr_simulation/maps/map.pgm'
        map1=Image.open(path)
        return map1
    
        
