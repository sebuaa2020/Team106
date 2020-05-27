class soundEquipment:
    def play(self):  #可以显示识别的关键词
        os.system("gnome-terminal -e 'bash -c \"roslaunch my_ speak _package speak.launch; exec bash\"'")
        
    def getText(self):  #获得self.text的值，作为后续确认
        #return self.text
        pass
