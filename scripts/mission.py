#!/usr/bin/env python

import time
from geometry_msgs.msg import Twist
import rospy


class no1:
    def __init__(self):
        self.topic_data = [[0, 0]]
        self.bool_data = False

    def callback(self, data):
        twist_data = data
        l = twist_data.linear.x
        a = twist_data.angular.z
        self.topic_data[0] = [l, a]
        self.bool_data = True

    def data_t(self):
        return self.topic_data

    def data_d(self):
        return self.bool_data

    def go(self):
        topic_publisher = rospy.Publisher("cmd_vel", Twist, queue_size=5)
        drive_data = Twist()
        drive_data.linear.x = self.topic_data[0][0]
        drive_data.angular.z = self.topic_data[0][1]
        topic_publisher.publish(drive_data)


def main():
    d = no1()
    o = no1()
    t = no1()
    n = no1()
    stop_num = 0
    rospy.init_node("mission_hub")
    rospy.Subscriber("o", Twist, o.callback)
    rospy.Subscriber("n", Twist, n.callback)
    rospy.Subscriber("d", Twist, d.callback)
    rospy.Subscriber("t", Twist, t.callback)

    while not rospy.is_shutdown():
        if t.bool_data == True:
            t.go()
        elif o.bool_data == True:
            cont = 0
            if stop_num == 0 or stop_num == 6 or stop_num == 14 or stop_num == 19 or stop_num == 11:
                print("1")
                while cont < 11:
                    topic_publisher = rospy.Publisher(
                        "cmd_vel", Twist, queue_size=5)
                    drive_data = Twist()
                    drive_data.linear.x = 0.1
                    drive_data.angular.z = 0.0
                    topic_publisher.publish(drive_data)
                    rate = rospy.Rate(10)
                    rate.sleep()
                    cont = cont+1
                time.sleep(6)
                stop_num += 1
            elif stop_num == 1 or stop_num == 7 or stop_num == 15 or stop_num == 20 or stop_num == 12:
                print("1_1")
                while cont < 30:
                    topic_publisher = rospy.Publisher(
                        "cmd_vel", Twist, queue_size=5)
                    drive_data = Twist()
                    drive_data.linear.x = 0.2
                    drive_data.angular.z = - 0.1
                    topic_publisher.publish(drive_data)
                    rate = rospy.Rate(10)
                    rate.sleep()
                    cont = cont+1
                stop_num += 1

            elif stop_num == 2 or stop_num == 5 or stop_num == 12 or stop_num == 16 or stop_num == 8 or stop_num == 9 or stop_num == 17:
                print("2")
                while cont < 5:
                    topic_publisher = rospy.Publisher(
                        "cmd_vel", Twist, queue_size=5)
                    drive_data = Twist()
                    drive_data.linear.x = 0.2
                    drive_data.angular.z = 0.0
                    topic_publisher.publish(drive_data)
                    rate = rospy.Rate(10)
                    rate.sleep()
                    cont = cont+1
                stop_num += 1

            elif stop_num == 3:
                print("3")
                time.sleep(3)
                if n.topic_data[0][0] > 0:
                    while cont < 45:
                        n.go()
                        rate = rospy.Rate(10)
                        rate.sleep()
                        cont = cont+1
                    cont = 0
                    while cont < 35:
                        topic_publisher = rospy.Publisher(
                            "cmd_vel", Twist, queue_size=5)
                        drive_data = Twist()
                        drive_data.linear.x = 0.2
                        drive_data.angular.z = -0.1
                        topic_publisher.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        cont = cont+1
                    stop_num = 12
                else:
                    print("red")
                    while cont < 10:
                        topic_publisher = rospy.Publisher(
                            "cmd_vel", Twist, queue_size=5)
                        drive_data = Twist()
                        drive_data.linear.x = 0.2
                        drive_data.angular.z = 0.0
                        topic_publisher.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        cont = cont+1
                    stop_num += 1
                    count = 0
                    while count < 90:
                        d.go()
                        count += 1
            elif stop_num == 4 or stop_num == 13:
                time.sleep(3)
                cont_1 = 0
                while cont_1 < 45:
                    n.go()
                    rate = rospy.Rate(10)
                    rate.sleep()
                    cont_1 = cont_1+1
                cont_1 = 0
                while cont_1 < 35:
                    topic_publisher = rospy.Publisher(
                        "cmd_vel", Twist, queue_size=5)
                    drive_data = Twist()
                    drive_data.linear.x = 0.2
                    drive_data.angular.z = -0.1
                    topic_publisher.publish(drive_data)
                    rate = rospy.Rate(10)
                    rate.sleep()
                    cont_1 = cont_1+1
                stop_num += 1
        elif stop_num == 10 or stop_num == 18:
            time_2 = time.time()
            while time.time() - time_2 < 20:
                d.go()
            if count_10 == 0:
                time.sleep(1)

                count = 0
                count_1 = 0
                count_2 = 0
                parking = False
                if parking == False:
                    count_12 = 0
                    count_123 = 0
                    while count_12 < 5:
                        drive_data = Twist()
                        drive_data.linear.x = -0.3
                        drive_data.angular.z = -0.2
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_12 += 1
                    while count_123 < 24:
                        drive_data = Twist()
                        drive_data.linear.x = -0.3
                        drive_data.angular.z = 1.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_123 += 1
                    while count_1 < 20:
                        drive_data = Twist()
                        drive_data.linear.x = -0.3
                        drive_data.angular.z = -1.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_1 += 1
                    while count < 8:
                        drive_data = Twist()
                        drive_data.linear.x = 0.2
                        drive_data.angular.z = -1.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count += 1
                    while count_2 < 4:
                        drive_data = Twist()
                        drive_data.linear.x = 0.2
                        drive_data.angular.z = 1.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_2 += 1
                    count_29 = 0
                    while count_29 < 1:
                        drive_data = Twist()
                        drive_data.linear.x = 0.2
                        drive_data.angular.z = 0.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_29 += 1
                    time.sleep(4)
                    count_35 = 0
                    while count_35 < 10:
                        drive_data = Twist()
                        drive_data.linear.x = -0.2
                        drive_data.angular.z = 0.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_35 += 1
                    time_2 = time.time()
                    while time.time() - time_2 < 2:
                        drive_data = Twist()
                        drive_data.linear.x = 0.2
                        drive_data.angular.z = 1.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()

                    count_3 = 0
                    while count_3 < 12:
                        drive_data = Twist()
                        drive_data.linear.x = 0.2
                        drive_data.angular.z = 0.4
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_3 += 1
                    count_4 = 0
                    while count_4 < 7:
                        drive_data = Twist()
                        drive_data.linear.x = 0.3
                        drive_data.angular.z = -1.0
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_4 += 1
                    count_5 = 0
                    while count_5 < 7:
                        drive_data = Twist()
                        drive_data.linear.x = 0.3
                        drive_data.angular.z = -0.4
                        cmd_vel_pub = rospy.Publisher(
                            'cmd_vel', Twist, queue_size=10)
                        cmd_vel_pub.publish(drive_data)
                        rate = rospy.Rate(10)
                        rate.sleep()
                        count_5 += 1
                        parking = True
                        count_10 += 1
            stop_num += 1

        else:
            d.go()
        t.bool_data = False
        o.bool_data = False
        rate = rospy.Rate(8)
        rate.sleep()


if __name__ == "__main__":
    main()
