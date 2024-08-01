#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

class LidarMotorController:
    def __init__(self):
        rospy.init_node('lidar_motor_controller', anonymous=True)
        self.pub = rospy.Publisher('/lidar_joint_velocity_controller/command', Float64, queue_size=10)
        self.rate = rospy.Rate(10)  # 10 Hz

    def run(self):
        while not rospy.is_shutdown():
            # Publie une vitesse constante pour une rotation continue
            self.pub.publish(Float64(1.0))  # 1 radian par seconde
            self.rate.sleep()

if __name__ == '__main__':
    try:
        controller = LidarMotorController()
        controller.run()
    except rospy.ROSInterruptException:
        pass