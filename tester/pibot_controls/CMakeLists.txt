cmake_minimum_required(VERSION 2.8.3)

if (POLICY CMP0048)
  cmake_policy(SET CMP0048 NEW)
endif (POLICY CMP0048)
project(pibot_controls VERSION 1.0.0)

find_package(roscpp REQUIRED)
find_package(std_msgs REQUIRED)
include_directories(${roscpp_INCLUDE_DIRS})
include_directories(${std_msgs_INCLUDE_DIRS})

# Load catkin and all dependencies required for this package
find_package(catkin REQUIRED COMPONENTS
)

catkin_package(
)
