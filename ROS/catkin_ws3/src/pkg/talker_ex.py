#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3
import random

class Talker:
    def __init__(self):
        rospy.init_node('talker', anonymous=True)
        self.pub = rospy.Publisher('exemplo', Vector3, queue_size=10)
        self.list = list(range(10))
    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            v = Vector3()
            v.x = random.choice(self.list) 
            v.y = random.choice(self.list) 
            v.z = random.choice(self.list)
            rospy.loginfo(p)
            self.pub.publish(p)
            rate.sleep()


if __name__ == '__main__':
    try:
        t = Talker()
        t.start()
    except rospy.ROSInterruptException:
        pass    