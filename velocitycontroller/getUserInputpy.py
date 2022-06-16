#!/usr/bin/env  python

import rospy
from std_msgs.msg import String

from geometry_msgs.msg import Twist

import sys
import termios
import tty

def publish_input():


	# Multiple actions 
	# We can go forward/backward in y using w/s
	# We can go left/right in x using a/d
	# We can go up/down in z using arrow keys
	
	pub = rospy.Publisher('/IsaacTestTopic', Twist, queue_size=10)
	rospy.init_node('velocity_publisher', anonymous=False);
	
	rate = rospy.Rate(20); # Publish at 20 Hz
	
	while (not rospy.is_shutdown()):
	
		data = Twist() # Create basic velocity command
		
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		
		
		if (ch == 'w'):
			data.linear.x = 0
			data.linear.y = 0.1
			data.linear.z = 0
		
			print("Increasing y")
		if (ch == 's'):
			data.linear.x = 0
			data.linear.y = -0.1
			data.linear.z = 0
			print("Decreasing y")
		if (ch == 'a'):
			data.linear.x = -0.1
			data.linear.y = 0
			data.linear.z = 0
			print("Decreasing x")
		if (ch == 'd'):
			data.linear.x = 0.1
			data.linear.y = 0
			data.linear.z = 0
			print("Hello d")
		if (ch == ' '):
			data.linear.x = 0
			data.linear.y =0
			data.linear.z = 0.1
			print("Hello Up")
		if (ch == 'v'):
			data.linear.x = 0
			data.linear.y = 0
			data.linear.z = -0.1
			print("Hello Down")
		if (ch == 'x'):
			data.linear.x = 0
			data.linear.y = 0
			data.linear.z = 0
			print("Emergency Stop")
			
		pub.publish(data)
		rate.sleep()
		
		
		
	
	
	
	
if __name__ == '__main__':
    try:
        publish_input()
    except rospy.ROSInterruptException:
        pass
	# End if