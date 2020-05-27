class camera():
    def takePicure(self):
        pass
    def analyse(self,item):  #物体检测
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials obj_detect.launch; exec bash\"'")
