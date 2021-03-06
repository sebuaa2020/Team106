## 四个乙方-ROS 机器人控制系统

### 项目简介

本项目为北京航空航天大学计算机学院 2020 年春季学期《软件工程》课程 106 组开发的项目。在课程组提供的 ROS 机器人等启智 ROS 机器人模拟器上开发一款实现开发能够通过手动按钮控制机器人运动或者语音控制机器人运动建立地图，机器人能够自动实时避障或者连续导航的简单机器人。

### 项目应用场景

- 商场或者餐厅引导机器人：在顾客到达之后，通过口头设置目标点，顾客可以跟随到达相应的消费点。
- 探测机器人：可利用自动避障机器人到达危险地区，进行拍照等操作。

### 运行环境

Ubuntu 16.04
python3.7

python 库：matpoltlib, time, subprocess，tkinter

安装 tkinter 命令

sudo apt-get update

sudo apt-get install python3-tk

### 源码获取

在 home 目录下新建文件夹 demo2_sc

git clone git@github.com:sebuaa2020/Team106.git

然后在～/demo2_sc/code/src/code 下执行 python3 GUI2.py

然后就会进入，用户名输入 123,密码 456，点击 login 按钮就能进入
点击 SLAM 建图，就会打开 rviz，gazebo 界面

### 功能特性

#### SLAM 建图

管理员点击 GUI 中“SLAM 地图”按钮后，选择“GUI 控制”或者“语音控制”，控制机器人运动，绕场地一周，建立地图。

#### 导航

用户点击 GUI 中“导航”按钮，选择“手动选择目标点”或者“连续导航”

- 手动选择目标点：设置起始点和目标点后，机器人自动规划路线到达指定地点，并在运动过程中实时避障。
- 连续导航：设置起始点，开始连续连续导航提示，点击”是“，机器人开始在设定的导航点下开始连续运动。手动也可修改航点位置和航点个数，在 wpr_simulation/src/simple_home_cruise.cpp 下的 Init_WayPoints()函数下可修改。

#### 语音控制

语音控制机器人运动

### 项目管理

小组前期主要使用微信群进行交流，后期增加了看板模块进行对项目的任务的发布。

## 文件夹规格.

### SDD

| **版本** | **提交日期** |     **主要编制人**     | **审核人** |            **版本说明**            |
| :------: | :----------: | :--------------------: | :--------: | :--------------------------------: |
|   v1.0   |  2020.4.19   |         章玉婷         |   王兆桓   |  完成数据库设计和需求可追踪性说明  |
|   v1.1   |  2020.4.19   |         章玉婷         |   陈雪青   |       详细化范围和需求概述,        |
|   v1.2   |  2020.4.19   |          图图          |   章玉婷   |       增加接口设计,修改类图        |
|   v1.3   |  2020.4.20   | 王兆桓、龚申勇、陈雪青 |   章玉婷   | 增加体系结构设计部分、详细设计部分 |
|   v1.4   |  2020.4.23   |         王兆桓         |   章玉婷   |        修改软件体系结构部分        |
|   v1.5   |  2020.5.19   |         王兆桓         |   章玉婷   |   完善运动导航部分，添加代码注解   |
|   v1.6   |  2020.5.19   |         章玉婷         |    图图    |        完善了 Slam 建图部分        |
|   v1.7   |  2020.5.20   |         陈雪青         |   龚申勇   |         完善了普通控制部分         |
|   v1.8   |  2020.5.20   |          图图          |   王兆桓   |  完善了路径规划模块和改修接口设计  |
|   V1.9   |  2020.5.20   |         陈雪青         |   龚申勇   |         完善了语音控制模块         |
|   V2.0   |   2020.6.8   |         陈雪青         |   章玉婷   |         完善了路径规划模块         |

### SDP

| **版本** | **提交日期** | **主要编制人** | **审核人** | **版本说明** |
| :------: | :----------: | :------------: | :--------: | :----------: |
|   V1.0   |   2020/3/8   |     王兆桓     |   章玉婷   |    第一版    |
|   V1.1   |  2020/3/24   |     王兆桓     |   章玉婷   |    第二版    |

### SRS

| **版本** | **提交日期** | **主要编制人** | **审核人** |               **版本说明**               |
| :------: | :----------: | :------------: | :--------: | :--------------------------------------: |
|   V1.0   |     4.1      |     陈雪青     |   章玉婷   |                 第一版本                 |
|   V1.1   |     4.6      |     章玉婷     |   陈雪青   |     增加了数据流图部分，详细化用例图     |
|   V1.2   |     4.6      |     章玉婷     |   陈雪青   | 详细，分层化了活动图，增加了用户界面部分 |
|   V1.3   |     4.7      |     章玉婷     |   陈雪青   |                 修改类图                 |
|   V1.4   |     6.8      |     章玉婷     |   王兆桓   |          类图修改、增加导航功能          |
|   V1.5   |     6.8      |     陈雪青     |   章玉婷   |    修改用例图、活动图，完善了各个部分    |

## STD

| **版本** | **提交日期** | **主要编制人** | **审核人** |           **版本说明**           |
| :------: | :----------: | :------------: | :--------: | :------------------------------: |
|   v1.0   |  2020.5.21   |     章玉婷     |   陈雪青   |        增加了任务概述部分        |
|   v1.1   |  2020.5.23   |      图图      |   章玉婷   |          增加了测试准备          |
|   v1.2   |  2020.5.23   |     陈雪青     |   王兆桓   |          增加了测试用例          |
|   v1.3   |  2020.5.26   |     龚申勇     |    图图    |          增加了测试结果          |
|   v1.4   |  2020.5.26   |     王兆桓     |   龚申勇   |        增加了测试结果分析        |
|   v1.5   |   2020.6.2   |     章玉婷     |    图图    | 完善了登录、注册、提示模块的测试 |
|   v1.6   |   2020.6.3   |     王兆桓     |   陈雪青   |       完善了路径导航的测试       |
|   v1.7   |   2020.6.3   |      图图      |   王兆桓   |       完善了主控模块的测试       |
|   v1.8   |   2020.6.5   |     王兆桓     |    图图    |          细化了测试内容          |
|   v1.9   |   2020.6.7   |     章玉婷     |   龚申勇   |        细化非功能需求部分        |
|   V2.0   |   2020.6.7   |     章玉婷     |   陈雪青   |      修改项目结构图，测试图      |

## PDSR \*

| ** 版本** | **提交日期** | **主要编制人** | **审核人** |      **版本说明**       |
| :-------: | :----------: | :------------: | :--------: | :---------------------: |
|   v1.0    |  2020.6.15   |     章玉婷     |   陈雪青   | 增加了 4.1,4.2.4.3 部分 |
|   v1.1    |  2020.6.15   |      图图      |   章玉婷   |  增加了 4.4,4.5.6 部分  |
|   v1.2    |  2020.6.15   |     王兆桓     |    图图    | 增加了 3.1,3.2,3.3 部分 |
|   v1.3    |  2020.6.16   |     章玉婷     |   龚申勇   |     完善了 4.1 部分     |
|   v1.4    |  2020.6.16   |      图图      |   王兆桓   |  完善了 4.4,4.5.6 部分  |
