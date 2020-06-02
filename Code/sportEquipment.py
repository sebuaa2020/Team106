import os
import threading
import subprocess
import time
class sportEquipment:
    def start(self):
        def start_move():
            self.pipe=subprocess.Popen("rosrun wpr_simulation keyboard_vel_ctrl",shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
        #os.system("source ../devel/setup.bash")
        #os.system("rosrun wpr_simulation keyboard_vel_ctrl")
        th = threading.Thread(target=start_move)
        th.setDaemon(True)
        th.start()
        
        
        
    def towards(self):
        def go_towards():
            self.pipe.stdin.write("w\n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_towards)#
        th.setDaemon(True)#保证了父进程被杀死后，子进程也会被杀死
        th.start()
        
    def backward(self):
        def go_backwards():
            self.pipe.stdin.write("s\n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_backwards)
        th.setDaemon(True)
        th.start()
    def left(self):
        def go_left():
            self.pipe.stdin.write("a\n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_left)#
        th.setDaemon(True)#保证了父进程被杀死后，子进程也会被杀死
        th.start()#如何将subprocess的输入即时发送到shell里面
        
    def right(self):
        def go_right():
            self.pipe.stdin.write("d\n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_right)
        th.setDaemon(True)
        th.start()
        #os.system("d -bash")
    def lev_acc(self):
        def go_lev_acc():
            self.pipe.stdin.write("q\n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_lev_acc)
        th.setDaemon(True)
        th.start()
        
        #os.system("q -bash")
    def ri_acc(self):
        def go_ri_acc():
            self.pipe.stdin.write("e\n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_ri_acc)
        th.setDaemon(True)
        th.start()
        #os.system("e -bash")
    def pause(self):
        def go_pause():
            self.pipe.stdin.write(" \n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_pause)
        th.setDaemon(True)
        th.start()
        #os.system("  -bash")
    def stop(self):
        def go_stop():
            self.pipe.stdin.write(" \n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
            self.pipe.stdin.write("x\n".encode())
            self.pipe.stdin.flush()
            time.sleep(1)
        th = threading.Thread(target=go_stop)
        th.setDaemon(True)
        th.start()
        #os.system("  -bash")
        #os.system("x -bash")

