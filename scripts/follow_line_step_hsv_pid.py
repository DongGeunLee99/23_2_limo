#!/usr/bin/env python

import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from std_msgs.msg import Float64
from move_robot import MoveKobuki
import time


kp = 0.002  # 0.0025
kd = 0.015
# ki = 1E-5 # kp * kp / (4 * kd)
ki = kp * kp / (4 * kd)  # Ziegler-Nichols method

class LineFollower(object):

    def __init__(self):
    
        self.bridge_object = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.error_x_pub = rospy.Publisher('/error_x', Float64, queue_size=10)
        self.movekobuki_object = MoveKobuki()
        self.error_x_object = Float64()
        self.old_cx = None
        self.count = 0
        self._sum = 0
        self._diff = 0
        self._last_err = 0

    def camera_callback(self,data):
        global kp, kd, ki
        
        try:
            # We select bgr8 because its the OpneCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)

        height, width, channels = cv_image.shape
        descentre = 140  # 220
        rows_to_watch = 50  # 20
        crop_img = cv_image[(height)//2+descentre:(height)//2+(descentre+rows_to_watch)][1:width]

        # Convert from RGB to HSV
        hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([20,100,100])
        upper_yellow = np.array([50,255,255])  # [30, 255, 255]

        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(crop_img,crop_img, mask= mask)

        # Calculate centroid of the blob of binary image using ImageMoments
        m = cv2.moments(mask, False)

        try:
            cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
        except ZeroDivisionError:
            cy, cx = height//2, width//2

        # Draw the centroid in the resultut image
        # cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]]) 
        cv2.circle(res, (int(cx), int(cy)), 10, (0,0,255), -1)

        # cv2.imshow("Original", cv_image)
        cv2.imshow("HSV", hsv)
        cv2.imshow("MASK", mask)
        cv2.imshow("RES", res)
        cv2.waitKey(1)

        error_x = width / 2 - cx
        error_x_object = Float64()
        error_x_object.data = error_x
        self._sum += error_x
        self._diff = error_x - self._last_err
        twist_object = Twist()
        twist_object.linear.x = 0.25
        twist_object.angular.z = error_x * kp + self._sum * ki + self._diff * kd
        self._last_err = error_x
        rospy.loginfo("ANGULAR VALUE SENT===>"+str(twist_object.angular.z))

        if cx == self.old_cx:
            self.count += 1
            if self.count >= 5:  # 10 
                twist_object.linear.x = 0.0
        self.old_cx = cx        
        time.sleep(2)
        # Make it start turning
        self.movekobuki_object.move_robot(twist_object)
        self.error_x_pub.publish(error_x_object)

    def clean_up(self):
        self.movekobuki_object.clean_class()
        cv2.destroyAllWindows()


def main():
    rospy.init_node('line_following_with_PID', anonymous=False)    
    line_follower_object = LineFollower()

    rate = rospy.Rate(5)
    ctrl_c = False

    def shutdownhook():
        # works better than the rospy.is_shut_down()
        line_follower_object.clean_up()
        rospy.loginfo("shutdown time!")
        ctrl_c = True
    
    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        rate.sleep()
    
    # try:
    #     rospy.spin()
    # except KeyboardInterrupt:
    #     print("Shutting down")
    # cv2.destroyAllWindows()

if __name__ == '__main__':
    main()