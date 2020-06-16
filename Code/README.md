# 代码文件夹

此文件夹包含用于 ROS 项目的所有代码文件。 它们也是其他核心模块，已经分为指定的文件夹。

**文件夹的详细说明如下：**

## _pycache_

此文件夹用于存储来自 python 的程序字节码。这些是我们程序的字节码编译版本和优化的字节码编译版本。**请忽略此文件夹**

## maps

这些文件夹用于地图。它包含用于动态连续导航的图片。还包含来自机器人使用的 GUI 的图片样本。还包含程序执行的快照 示例图片如下所示：

![alt text](https://github.com/sebuaa2020/Team106/blob/master/Code/maps/finish.jpg "GUI Logo")

## voice_ctrl

ROS 机器人具有语音控制功能，该功能在此文件夹中实现。 该文件夹包含用于语音控制的 ROS 节点，并以 C ++编程语言实现。

## wpr_simulation

带**rviz**的模拟文件夹，它是机器人操作系统（ROS）框架的 3D 可视化工具。

**代码文件用于不同的模块，如下所述：**

### GUI

这是机器人的 GUI 的实现。 GUI2.py 使用带有 Tkinter 的 python 3 实现。 因此，在尝试运行该程序以确保已使用 python 3 运行该程序时非常重要。

### 导航

- path planning
  机器人路线计划功能是通过`routeplan.py`文件实现的.

- 连续导航
  导航是通过 **navigation**文件实现的，并具有连续导航支持。`simple_home_cruise.cpp`文件具有连续导航功能的实现。

- 语音识别
  ROS 机器人具有语音识别功能，使我们的机器人能够基于实时语音活动检测算法执行高可靠性的实时语音识别，效率高且计算资源消耗低。通过麦克风，GUI 可以显示识别的 关键词。 识别的单词由 `soundEquipment.py`和手动利用按钮建图；语音控制建图来处理。基本的导航功能。语音控制机器人运动功能。

- SLAM
  SLAM 由`slamMap.py`处理，该工具执行许多功能，但主要处理地图。 在需要时保存地图。

开启 slam 建图 :
![alt text](https://github.com/sebuaa2020/Team106/blob/master/Code/slam_start.jpg "SLAM")

### 系统测试

我们对机器人进行了各种测试，其中一些文件（例如`test.py`，`test_keyboard_vel.cpp`）专门用于系统测试。
