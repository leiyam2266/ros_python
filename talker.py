#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random

def talker():
	rospy.init_node('talker_node', anonymous=True)
	pub = rospy.Publisher('random_num', String, queue_size=10)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		nub = random.randint(0, 1000)
		if (nub>500):
			re="over 500"
		elif(nub==500):
			re="equivalent to 500"
		else:
			re="less than 500"
		msg=("The number generated is "+re+" :"+str(nub))
		rospy.loginfo("Data sent")
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
