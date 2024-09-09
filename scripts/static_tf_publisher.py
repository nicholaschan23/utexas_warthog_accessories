#!/usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped

def static_tf_publisher():
    rospy.init_node('static_tf_publisher')

    static_broadcaster = tf2_ros.StaticTransformBroadcaster()

    # Define the static transform
    front_lidar = initTransform()
    front_lidar.header.frame_id = "bulkhead_front_mount_link"
    front_lidar.child_frame_id = "front_lidar_link"

    # Broadcast the static transforms
    static_broadcaster.sendTransform(front_lidar) # [transform1, transform2]
    
    rospy.spin()  # Keep the node alive


def initTransform(tx=0.0, ty=0.0, tz=0.0, rx=0.0, ry=0.0, rz=0.0, rw=1.0):
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()

    # Set the translation (x, y, z)
    transform.transform.translation.x = tx
    transform.transform.translation.y = ty
    transform.transform.translation.z = tz
    
    # Set the rotation (quaternion: x, y, z, w)
    transform.transform.rotation.x = rx
    transform.transform.rotation.y = ry
    transform.transform.rotation.z = rz
    transform.transform.rotation.w = rw

    return transform

if __name__ == '__main__':
    try:
        static_tf_publisher()
    except rospy.ROSInterruptException:
        pass
