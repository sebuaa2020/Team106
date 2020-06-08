#!/usr/bin/env python

import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from random import sample
from math import pow, sqrt

class NavTest():
    def __init__(self):
        #节点名称
        rospy.init_node('navigation', anonymous=True)
        #处理关闭时，调用myhook函数
        rospy.on_shutdown(myhook)

        locations = dict()
        
        locations['b1'] = Pose(Point(0.643, 4.720, 0.000), Quaternion(0.000, 0.000, 0.223, 0.975))
        locations['kitchen'] = Pose(Point(-1.994, 4.382, 0.000), Quaternion(0.000, 0.000, -0.670, 0.743))
        locations['bedroom'] = Pose(Point(-3.719, 4.401, 0.000), Quaternion(0.000, 0.000, 0.733, 0.680))
        locations['living1'] = Pose(Point(0.720, 2.229, 0.000), Quaternion(0.000, 0.000, 0.786, 0.618))
        locations['living2'] = Pose(Point(1.471, 1.007, 0.000), Quaternion(0.000, 0.000, 0.480, 0.877))
        locations['living3'] = Pose(Point(1.029, 0.450, 0.000), Quaternion(0.000, 0.000, 0.682, 0.587))
        locations['dining1'] = Pose(Point(-0.861, -0.019, 0.000), Quaternion(0.000, 0.000, 0.892, -0.451))

        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        
        #等60s
        self.move_base.wait_for_server(rospy.Duration(60))
        
        rospy.loginfo("Connected to move base server")
        
        initial_point = PoseWithCovarianceStamped()
        
        localen = len(locations)
i = localen
        j = 0
        n_successes = 0
        location = ""
        lalocal = ""
        
        #得到起点信息
        rospy.loginfo("set the starting point")
        rospy.wait_for_message('initialpoint', PoseWithCovarianceStamped)
        self.lalocal = Pose()
        rospy.Subscriber('initialpoint', PoseWithCovarianceStamped, self.update_initial_pose)
        
        while not rospy.is_shutdown():
            if i == n_localen:
                i = 0
                sequence = sample(locations, localen)
                if sequence[0] == lalocal:
                    i = 1
            
            location = sequence[i]
                        
            if initial_pose.header.stamp == "":
                distance = sqrt(pow(locations[location].position.x - 
                                    locations[lalocal].position.x, 2) +
                                pow(locations[location].position.y - 
                                    locations[lalocal].position.y, 2))
            else:
                rospy.loginfo("Updating current pose.")
                distance = sqrt(pow(locations[location].position.x - 
                                    initial_pose.pose.pose.position.x, 2) +
                                pow(locations[location].position.y - 
                                    initial_pose.pose.pose.position.y, 2))
                initial_pose.header.stamp = ""
            
            #每一时刻到达的终点
            lalocal = location
            
            i += 1
            j += 1
            #要到达的下一目的地
            self.goal = MoveBaseGoal()
            self.goal.target_pose.pose = locations[location]
            self.goal.target_pose.header.frame_id = 'map'
            self.goal.target_pose.header.stamp = rospy.Time.now()

            self.move_base.send_goal(self.goal)
            
    def update_initial_pose(self, initial_pose):
        self.initial_pose = initial_pose

    def myhook():
        rospy.loginfo("Stopping the robot...")
        self.move_base.cancel_goal()
        rospy.sleep(2)
        self.cmd_vel_pub.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        NavTest()
        rospy.spin()
    except rospy.ROSInterruptException:

