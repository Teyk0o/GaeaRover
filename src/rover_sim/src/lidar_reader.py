#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import ByteMultiArray

class TFminiPlusSimulator:
    def __init__(self):
        rospy.init_node('tfmini_plus_simulator', anonymous=True)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.laser_callback)
        self.pub = rospy.Publisher('/tfmini_data', ByteMultiArray, queue_size=10)
        
    def laser_callback(self, msg):
        if len(msg.ranges) > 0:
            distance = int(msg.ranges[0] * 100)  # Convert to cm
            strength = 100  # Example signal strength value
            temp = 25  # Example temperature
            
            # TFmini Plus standard format (9 bytes)
            data = [0x59, 0x59,
                    distance & 0xFF, (distance >> 8) & 0xFF,
                    strength & 0xFF, (strength >> 8) & 0xFF,
                    temp & 0xFF, (temp >> 8) & 0xFF,
                    0]  # Checksum (to be calculated)
            
            # Calculate checksum
            data[-1] = sum(data[:-1]) & 0xFF
            
            output_msg = ByteMultiArray()
            output_msg.data = data
            self.pub.publish(output_msg)
            
            # Log the data for debugging
            rospy.loginfo(f"Distance: {distance} cm, Strength: {strength}, Temp: {temp}")

def main():
    try:
        simulator = TFminiPlusSimulator()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()