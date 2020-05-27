import os
import threading
class sportEquipment:
    def towards(self):
        def go_towards():
            os.system("w")
        th = threading.Thread(target=go_towards)
        th.setDaemon(True)
        th.start()
        
    def backward(self):
        def go_backwards():
            os.system("s -bash")
        th = threading.Thread(target=go_backwards)
        th.setDaemon(True)
        th.start()
        
    def left(self):
        def go_left():
            os.system("a -bash")
        th = threading.Thread(target=go_left)
        th.setDaemon(True)
        th.start()
        
    def right(self):
        def go_right():
            os.system("d -bash")
        th = threading.Thread(target=go_right)
        th.setDaemon(True)
        th.start()
        #os.system("d -bash")
    def lev_acc(self):
        def go_lev_acc():
            os.system("q -bash")
        th = threading.Thread(target=go_lev_acc)
        th.setDaemon(True)
        th.start()
        #os.system("q -bash")
    def ri_acc(self):
        def go_ri_acc():
            os.system("e -bash")
        th = threading.Thread(target=go_ri_acc)
        th.setDaemon(True)
        th.start()
        #os.system("e -bash")
    def pause(self):
        def go_pause():
            os.system("  -bash")
        th = threading.Thread(target=go_pause)
        th.setDaemon(True)
        th.start()
        #os.system("  -bash")
    def stop(self):
        def go_stop():
            os.system("  -bash")
            os.system("x -bash")
        th = threading.Thread(target=go_stop)
        th.setDaemon(True)
        th.start()
        #os.system("  -bash")
        #os.system("x -bash")

