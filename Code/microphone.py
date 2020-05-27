class microphone:
    def __init__(self):
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials speech_recognition.launch; exec bash\"'")
    def voice2text(self):  #可以显示识别的关键词  
        return "桌子" 
