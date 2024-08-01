cmake_minimum_required(VERSION 3.0.2)
project(rover_sim)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  gazebo_ros
  velocity_controllers
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs gazebo_ros
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/lidar_reader.py
  src/lidar_motor_controller.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)