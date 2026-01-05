#!/usr/bin/env python
"""Simple test to verify /scan topic is working and has valid point data."""

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import sys

received_count = [0]
total_points = [0]

def callback(cloud):
    received_count[0] += 1
    point_count = cloud.width * cloud.height
    total_points[0] += point_count
    
    # Try to extract a few points to verify data is valid
    try:
        points = list(pc2.read_points(cloud, field_names=("x", "y", "z"), skip_nans=True))
        valid_points = len(points)
        
        rospy.loginfo("Message %d: %d total points, %d valid (x,y,z) points", 
                      received_count[0], point_count, valid_points)
        if received_count[0] <= 3:
            if len(points) > 0:
                rospy.loginfo("  First point: x=%.3f, y=%.3f, z=%.3f", 
                             points[0][0], points[0][1], points[0][2])
    except Exception as e:
        rospy.logerr("Error reading points: %s", str(e))

def main():
    rospy.init_node('scan_test_subscriber')
    rospy.loginfo("Subscribing to /scan...")
    
    sub = rospy.Subscriber('/scan', PointCloud2, callback, queue_size=1)
    
    try:
        rospy.loginfo("Listening for 10 seconds...")
        rospy.sleep(10)
    except KeyboardInterrupt:
        pass
    
    rospy.loginfo("Test complete. Total messages: %d, Total points: %d", 
                  received_count[0], total_points[0])
    
    if received_count[0] == 0:
        rospy.logerr("ERROR: No messages received from /scan!")
        sys.exit(1)
    elif total_points[0] == 0:
        rospy.logerr("ERROR: Received messages but no valid points!")
        sys.exit(1)
    else:
        rospy.loginfo("SUCCESS: /scan is publishing valid point data")
        sys.exit(0)

if __name__ == '__main__':
    main()
