## 四个乙方-ROS机器人控制系统

### 项目简介

本项目为北京航空航天大学计算机学院2020年春季学期《软件工程》课程106组开发的项目。在课程组提供的ROS机器人等启智ROS机器人模拟器上开发一款实现开发能够通过手动按钮控制机器人运动或者语音控制机器人运动建立地图，机器人能够自动实时避障或者连续导航的简单机器人。

### 项目应用场景

- 商场或者餐厅引导机器人：在顾客到达之后，通过口头设置目标点，顾客可以跟随到达相应的消费点。
- 探测机器人：可利用自动避障机器人到达危险地区，进行拍照等操作。

### 运行环境

Ubuntu 16.04
python3.7 

python库：matpoltlib, time, subprocess，tkinter

安装tkinter命令

sudo apt-get update

sudo apt-get install python3-tk

### 源码获取

在home目录下新建文件夹demo2_ws

git clone git@github.com:sebuaa2020/Team106.git

然后在～/demo2_ws/src/code下执行python3 GUI2.py

![img](file:///C:/Users/27221/AppData/Local/Packages/microsoft.office.desktop_8wekyb3d8bbwe/AC/%23!oice_16_974fa576_32c1d314_1905/Temp/msohtmlclip1/01/clip_image002.jpg)



然后就会进入这，用户名输入123,密码456，点击login按钮就能进入图3

<img src="file:///C:/Users/27221/AppData/Local/Packages/microsoft.office.desktop_8wekyb3d8bbwe/AC/%23!oice_16_974fa576_32c1d314_1905/Temp/msohtmlclip1/01/clip_image004.jpg" alt="img" style="zoom:33%;" />

 																						图2

点击SLAM建图，就会打开rviz，gazebo界面，如图4

![img](file:///C:\Users\27221\AppData\Local\Temp\ksohtml14824\wps1.jpg)

​																							图4

 

 

### 功能特性

#### SLAM建图

管理员点击GUI中“SLAM地图”按钮后，选择“GUI控制”或者“语音控制”，控制机器人运动，绕场地一周，建立地图。

#### 导航

用户点击GUI中“导航”按钮，选择“手动选择目标点”或者“连续导航”

- 手动选择目标点：设置起始点和目标点后，机器人自动规划路线到达指定地点，并在运动过程中实时避障。
- 连续导航：设置起始点，开始连续连续导航提示，点击”是“，机器人开始在设定的导航点下开始连续运动。手动也可修改航点位置和航点个数，在wpr_simulation/src/simple_home_cruise.cpp下的Init_WayPoints()函数下可修改。

#### 语音控制

语音控制机器人运动


### 项目代码结构

![img](file:///C:\Users\27221\AppData\Local\Temp\ksohtml14824\wps2.jpg)

### 项目管理

小组前期主要使用微信群进行交流，后期增加了看板模块进行对项目的任务的发布。