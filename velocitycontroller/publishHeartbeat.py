#!/usr/bin/env  python

import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist


class listener():
	def __init__(self):
		self.msg = ""
		self.pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=10)
		self.sub = rospy.Subscriber('/IsaacTestTopic', Twist, self.update_msg)
		rospy.init_node('velocity_subscriber', anonymous=False);
		self.data = Twist()
	
	def run_heartbeat(self):
	# Sole purpose to to transmit messages if no user input

		
		
		rate = rospy.Rate(20); # Publish at 2 Hz
		
		while not rospy.is_shutdown():
		
			self.pub.publish(self.data)
			rate.sleep()
	

	def update_msg(self, received_msg):
		self.data = received_msg
		
	
		

def run_heartbeat():
	
	mySubscriber = listener()
	try:
		mySubscriber.run_heartbeat()
	except rospy.ROSInterruptException:
		pass
	
	
if __name__ == '__main__':
    run_heartbeat()
    
	# End if