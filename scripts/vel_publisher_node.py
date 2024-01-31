#!/usr/bin/env python3

# ROS imports
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('vel_publisher_node', anonymous=True)

    # Declare a publisher to publish on the velocity command topic
    cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Set a 10Hz frequency for the control loop
    loop_rate = rospy.Rate(10)

    # Declare a variable of type Twist for sending control commands
    vel_cmd = Twist()

    # Control loop
    while not rospy.is_shutdown():
        # Set the linear (forward/backward) velocity command
        vel_cmd.linear.x = 0.5

        # Set the angular (rotational) velocity command
        vel_cmd.angular.z = 0.5

        # Publish the command to the defined topic
        cmd_pub.publish(vel_cmd)

        # Wait for 0.1 seconds until the next loop iteration
        loop_rate.sleep()
