# octomap_small_time
Traditional octomaps, due to the accumulation of point clouds, can cause noticeable lag on some lower-performance computers. We have modified the code to make the point cloud representation of obstacles in the octomap single-frame.The specific configuration process is as follows:
  
  1.sudo apt-get install ros-noetic-octomap*
  
  2.mkdir octomap_ws
  
  3.cd octomap_ws
  
  4.mkdir src
  
  5.cd src
  
  6.git clone https://github.com/everaright/octomap_single_frame.git
	
  7.cd ..
	
  8.catkin_make

  Thus, we have completed all the configuration work.Next, we will demonstrate how to use this octomap.

  1.cd octomap_ws

  2.source devel/setup.bash

  3.roslaunch octomap_server 

  4.roslaunch octomap_server octomap_lidar_test.launch 

  At this point, we have completed the entire process.

Please note that in the octomap_lidar_test.launch , the coordinate system and point cloud topic name need to be modified according to your actual setup. Most importantly, remember that it can only process point clouds of the type pointcloud2!

  
