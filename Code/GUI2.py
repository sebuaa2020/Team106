import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import pickle
import os
import time
from PIL import Image
import matplotlib.pyplot as plt
import navigation
import sportEquipment
import slamMap
import soundEquipment
#import microPhone
'''import navigation
import sportEquipment
import microPhone
import camera'''
SYS=False
USR=False

target_x=0
target_y=0
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('ROS机器人控制程序')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('400x300')  # 这里的乘是小x
 
# 第4步，加载 welcome image

canvas = tk.Canvas(window, width=400, height=135, bg='white')
image_file = tk.PhotoImage(file='logo.png')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
canvas.pack(side='top')
tk.Label(window, text='四个乙方',font=('Arial', 16)).pack()
 
# 第5步，用户信息
usr_name_label=tk.Label(window, text='User name:', font=('Arial', 14))
usr_name_label.place(x=10, y=170)
usr_pw_label=tk.Label(window, text='Password:', font=('Arial', 14))
usr_pw_label.place(x=10, y=210)
# 第6步，用户登录输入框entry
# 用户名
var_usr_name = tk.StringVar()
#var_usr_name.set('example@163.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.place(x=120,y=175)
# 用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.place(x=120,y=215)



def build_map():  #还有一些按钮没有实现
    def stop_map(top,spt_ep):
        top.destroy()
        spt_ep.stop()
    def buildmap_info():
        tkinter.messagebox.showinfo(title='提示', message='请控制机器人绕场一周，使得不存在灰色区域')
        
    m=slamMap.slamMap()
    m.buildMap()
    image_info = tk.PhotoImage(file='info.gif')
    
    top = tk.Toplevel()
    spt_ep=sportEquipment.sportEquipment()
    btninfo=tk.Button(top,width=20,height=20,image=image_info,command=buildmap_info)
    btninfo.grid(row=0,column=2)
    bnt1=tk.Button(top,text="向前加速",command=spt_ep.towards)
    bnt1.grid(row=1,column=1)
    #bnt1.pack()
    bnt3=tk.Button(top,text="向左加速",command=spt_ep.left)
    bnt3.grid(row=2,column=0)
    #bnt3.pack(side=tk.LEFT)
    bnt4=tk.Button(top,text="向右加速",command=spt_ep.right)
    bnt4.grid(row=2,column=2)
    #bnt4.pack(side=tk.RIGHT)
    bnt2=tk.Button(top,text="向后加速",command=spt_ep.backward)
    bnt2.grid(row=3,column=1)
    #bnt2.pack()
    bnt5=tk.Button(top,text="左旋加速",command=spt_ep.pause)
    bnt5.grid(row=4,column=0)
    #bnt5.pack(side=tk.LEFT)
    bnt6=tk.Button(top,text="右旋加速",command=spt_ep.stop)
    bnt6.grid(row=4,column=2)
    #bnt6.pack(side=tk.RIGHT)
    bnt7=tk.Button(top,text="刹车",command=spt_ep.stop)
    bnt7.grid(row=5,column=0)
    #bnt7.pack()
    bnt8=tk.Button(top,text="退出",command=lambda:stop_map(top,spt_ep))
    bnt8.grid(row=5,column=2)
    #bnt8.pack()
    top.mainloop()
    
        

def voice_ctl():
    soundEquipment.


def load_map():
    path=os.getcwd()+'\maps\example.png'
    image=Image.open(path)
    plt.imshow(image)
    
def get_target():  #设置目标点，
    def back(surwin):
        surwin.destroy()
        get_target()
    
    pos=plt.ginput(1)
    target_x=pos[0][0]
    target_y=pos[0][1]
    surewin=tk.Toplevel()
    surewin.title("确定选择该终点？")
    bnt1=tk.Button(surewin,text="确定",command=surewin.destroy)
    bnt1.pack(side=tk.LEFT)
    bnt2=tk.Button(surewin,text="返回",command=lambda:back(surewin))
    bnt2.pack(side=tk.RIGHT)
    surewin.mainloop()


    
    
def navigate():
    load_map()
    get_target()
    nav=navigation.navigation()
    nav.navigate()
    sp_eq=sportEquipment.sportEquipment()
    surewin=tk.Tk()
    surewin.title('开始进行')
    surewin.geometry('400x300')
    bnt1=tk.Button(surewin,text="暂停",command=sp_eq.pause)
    bnt1.pack()
    bnt2=tk.Button(surewin,text="停止",command=sp_eq.stop)
    bnt2.pack()
    surewin.mainloop()
   

def menu():
    global bnt1,bnt2,bnt3
    bnt1=tk.Button(window, text='SLAM建图', command=build_map)
    bnt1.pack()
    bnt2=tk.Button(window,text='导航',command=navigate)
    bnt2.pack()
    bnt3=tk.Button(window,text='语音控制',command=voice_ctl)
    bnt3.pack()    
 
# 第8步，定义用户登录功能
def usr_login():
    def destroy_login():
        entry_usr_name.destroy()
        entry_usr_pwd.destroy()
        usr_pw_label.destroy()
        usr_name_label.destroy()
        btn_login.destroy()
        btn_sign_up.destroy()
        
    # 这两行代码就是获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
 
    # 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
    # 中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        # 这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
        # 的用户和密码写入，即用户名为`admin`密码为`admin`。
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()    # 必须先关闭，否则pickle.load()会出现EOFError: Ran out of input
 
    # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            
            tkinter.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
            destroy_login()
            menu()
        # 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:  # 如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
        # 提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()
 
# 第9步，定义用户注册功能
def usr_sign_up():
    def sign_to_Hongwei_Website():
        # 以下三行就是获取我们注册时所输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
 
        # 这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
        if np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')
 
        # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')
 
        # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然后销毁窗口。
            window_sign_up.destroy()
            
 
    # 定义长在窗口上的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')
 
    new_name = tk.StringVar()  # 将输入的注册名赋值给变量
    new_name.set('example@163.com')  # 将最初显示定为'example@163.com'
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_new_name.place(x=130, y=10)  # `entry`放置在坐标（150,10）.
 
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)
 
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)
 
    # 下面的 sign_to_Hongwei_Website
    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Hongwei_Website)
    btn_comfirm_sign_up.place(x=180, y=120)
 
# 第7步，login and sign up 按钮
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120, y=240)
bnt1=bnt2=bnt3=bnt4=bnt5=bnt6=btn_login
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=200, y=240)
#image_info = tk.PhotoImage(file='info.gif')
#btninfo=tk.Button(window,width=10,height=10,image=image_info)
#btninfo.place(x=280,y=240)
# 第10步，主窗口循环显示
window.mainloop()
