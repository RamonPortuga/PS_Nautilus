#!/usr/bin/env python3

import rospy
import math
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32

class Listener():
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('nautilus', Vector3, self.callback)
        self.pub = rospy.Publisher('resultado', Float32, queue_size=10)

    def callback(self, msg):
        x, y, z = msg.x, msg.y, msg.z
        total_potencia = pow(x, 2) + pow(y, 2) + pow(z, 2)
        raiz = math(total_potencia)
        modulo = fabs(raiz)
        f = Float32()
        f.data = total
        rospy.loginfo(f)
        self.pub.publish(f)

if __name__ == '__main__':
    l = Listener()
    rospy.spin()