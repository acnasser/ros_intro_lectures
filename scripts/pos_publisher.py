#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from ros_intro_lectures.msg import Shortpose
import math

# Conversion factor for radians to degrees
ROTATION_SCALE = 180.0 / math.pi

pos_msg = Shortpose()

def pose_callback(data):
	global pos_msg
	pos_msg.theta = data.theta * ROTATION_SCALE
	pos_msg.x = data.x * 100 
	pos_msg.y = data.y* 100		
    

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('pos_converter', anonymous=True)

    # Subscribe to the TurtleSim Pose topic
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    pos_pub = rospy.Publisher('/turtle1/shortpose', Shortpose, queue_size = 10)
    
    loop_rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
    	pos_pub.publish(pos_msg)
    	loop_rate.sleep()
