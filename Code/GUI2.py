#!/usr/bin/python
# -*- coding: utf-8 -*-
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
#import navigation
import sportEquipment
import microphone
import camera
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
image_file = tk.PhotoImage(file='logo.PNG')
image = canvas.create_image(200, 0, anchor='n', image=image_file)
#canvas.place(x=0,y=0)
canvas.pack(side='top')
tk.Label(window, text='四个乙方',font=('Arial', 16)).pack()
image_info = tk.PhotoImage(file='info.gif')

def main_info():
    def message(t,m):
        tk.messagebox.showinfo(title=t,message=m)
    helps=['功能介绍','slam建图','导航','联系我们']
    messages=['请选择slam建图或者导航',
              'slam建图用于建立当前所在空间的地图',
              '导航用于控制机器人到指定的目标点\n'+'导航之前需要确定是否曾经保存过当前区域的地图\n'+'如果没有，请先选择slam建图',
              '开发人员信息      邮箱\n'+
              '章玉婷            17231087@buaa.edu.cn']
    top=tk.Toplevel()
    bnt1=tk.Button(top,text=helps[0],command=lambda:message(helps[0],messages[0]))
    bnt1.pack()
    bnt2=tk.Button(top,text=helps[1],command=lambda:message(helps[1],messages[1]))
    bnt2.pack()
    bnt3=tk.Button(top,text=helps[2],command=lambda:message(helps[2],messages[2]))
    bnt3.pack()
    bnt4=tk.Button(top,text=helps[3],command=lambda:message(helps[3],messages[3]))
    bnt4.pack()
    

mb = tk.Button(window,width=10,height=10,image=image_info,command=main_info)
mb.place(x=380,y=0)
#mb = tk.Button(window,width=10,height=10,image=image_info,command=lambda:main_info(helps,messages)) 


#btninfo=tk.Button(window,width=10,height=10,image=image_info,command=main_info)
#btninfo.place(x=280,y=10)
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

def bulid_map_voice(topp):
    def save_map():
        
        top.destroy()
        
        m.save_map()
    topp.destroy()
    top=tk.Toplevel()
    top.title("语音控制开启")
    tk.Label(top, text="请通过语音控制控制机器人绕场一周，使得rviz地图中不存在灰色区域\n"+
    "之后可选择保存地图 or 不保存地图\n"
    "可输入语音指令关键词代表信息：\n"+
    "前——机器人前进\n"+
    "后——机器人后退\n"+
    "左——机器人向左转\n"+
    "右——机器人向右转\n"+
    "停——机器人停止运动\n",font=('Arial', 8)).pack()
    bnt1=tk.Button(top,text="保存地图",command=save_map)
    bnt1.pack(side=tk.LEFT)
    bnt2=tk.Button(top,text="不保存地图",command=top.destroy)
    bnt2.pack(side=tk.RIGHT)
    
    m=slamMap.slamMap()
    m.buildMap()
    time.sleep(1)
    soundE=soundEquipment.soundEquipment()
    soundE.start()
    

def quit_save(topw):
    top=tk.Toplevel()
    top.time("sure?")
    bnt1=tk.Button(top,text="sure",command=(top.destroy and topw.destroy))
    bnt1.pack()
    bnt2=tk.Button(top,text="cancel",command=top.destroy)
    bnt2.pack()
    
def build_map_manual(topp):  #还有一些按钮没有实现
    def save_map():
        
        top.destroy()
        
        m.save_map()

    def stop_map(top,spt_ep):
        top.destroy()
        spt_ep.stop()
        topw=tk.Toplevel()
        topw.title('提示')
        label=tk.Label(topw,text="是否保存地图？",font=('Arial', 8))
        label.pack()
        bnt1=tk.Button(topw,text="是",command=save_map)
        bnt1.pack(side=tk.LEFT)
        bnt2=tk.Button(topw,text="否",command=topw.destroy)
        bnt2.pack(side=tk.RIGHT)

    def buildmap_manual_info():
        tkinter.messagebox.showinfo(title='提示', message='请通过按钮控制机器人绕场一周，使得rviz地图中不存在灰色区域')
    topp.destroy()  
    m=slamMap.slamMap()
    m.buildMap()
    
    top = tk.Toplevel()
    
    spt_ep=sportEquipment.sportEquipment()
    spt_ep.start()
    btninfo=tk.Button(top,width=20,height=20,image=image_info,command=buildmap_manual_info)
    btninfo.grid(row=0,column=2)
    bnt1=tk.Button(top,text="向前加速",command=spt_ep.towards)
    bnt1.grid(row=1,column=1)
    
    bnt3=tk.Button(top,text="向左加速",command=spt_ep.left)
    bnt3.grid(row=2,column=0)
    
    bnt4=tk.Button(top,text="向右加速",command=spt_ep.right)
    bnt4.grid(row=2,column=2)
    
    bnt2=tk.Button(top,text="向后加速",command=spt_ep.backward)
    bnt2.grid(row=3,column=1)
    
    bnt5=tk.Button(top,text="左旋加速",command=spt_ep.lev_acc)
    bnt5.grid(row=4,column=0)
   
    bnt6=tk.Button(top,text="右旋加速",command=spt_ep.ri_acc)
    bnt6.grid(row=4,column=2)
    
    bnt7=tk.Button(top,text="刹车",command=spt_ep.stop)
    bnt7.grid(row=5,column=0)
    
    bnt8=tk.Button(top,text="退出",command=lambda:stop_map(top,spt_ep))
    bnt8.grid(row=5,column=2)
    
    top.mainloop()
def build_map():
    top=tk.Toplevel()
    top.title("选择控制机器人类型")
    bnt1=tk.Button(top,text="ＧＵＩ按钮控制",command=lambda:build_map_manual(top))  
    bnt1.pack()
    bnt2=tk.Button(top,text="语音控制",command=lambda:bulid_map_voice(top))
    bnt2.pack() 
    top.mainloop()
def navigation1():
    nav=navigation.navigation()
    nav.navigate()
    sp_eq=sportEquipment.sportEquipment()
    os.system("rosrun wpr_simulation keyboard_vel_ctrl")
    #surewin=tk.Tk()
    '''surewin=tk.Toplevel()
    surewin.title('开始进行')
    surewin.geometry('400x300')
    sp_eq.start()#start control
    bnt1=tk.Button(surewin,text="暂停",command=sp_eq.pause)#???
    bnt1.pack()
    bnt2=tk.Button(surewin,text="停止",command=sp_eq.stop)#???
    bnt2.pack()
    surewin.mainloop()'''
    
    

   
def navigateType():
    def navigate_info():  #hai mei xie 
        pass 
    def manual_ctrl():
        '''def load_map():  #加载当前地图
            path=os.getcwd()+'/maps/map.pgm'
            image=Image.open(path)
            plt.imshow(image)
    
        def get_target():  #手动设置目标点，
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
            print(target_x,target_y)
            bnt2=tk.Button(surewin,text="返回",command=lambda:back(surewin))
            bnt2.pack(side=tk.RIGHT)
            surewin.mainloop()'''
        top.destroy()
        #load_map()
        #get_target()
        navigation1()      
    def voice_ctrl():  
        top.destroy()
        mic=microphone.microphone()
        item=mic.voice2text()
        sep=soundEquipment()
        sep.play(item)  #确定是否是该物品，如何将
        targetx,targety=camera.anaylse(item)
        str1="经分析该物体在"+str(targetx)+str(targety)+"位置,是否确定选择该终点"
        sep.play(str1)
        ans=mic.voice2text()
        if ans=="是":
            navigation1(targetx,targety)
        else:
            voice_ctrl()  
        
        
    top=tk.Toplevel()
    top.title("导航类型选取")
    btninfo=tk.Button(top,width=10,height=10,image=image_info,command=navigate_info)  #导航信息提示
    btninfo.place(x=280,y=10)
    btn1=tk.Button(top,text="手动选取目标点",command=manual_ctrl)
    btn1.pack()
    btn2=tk.Button(top,text="语音选取目标点",command=voice_ctrl)
    btn2.pack()
def voice_ctl():
    soundE=soundEquipment.soundEquipment()
    soundE.start()
    
def menu():
    global bnt1,bnt2,bnt3
    bnt1=tk.Button(window, text='SLAM建图', command=build_map)
    bnt1.pack()
    bnt2=tk.Button(window,text='导航',command=navigateType)
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

# 第10步，主窗口循环显示
window.mainloop()
