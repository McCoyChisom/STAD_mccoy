cmake_minimum_required(VERSION 3.15)

# Specify your project's name
project(STAD_mccoychisom)

# Specify at least C++17 (better to use C++17 for newer MAVSDK features)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable strict handling of warnings
add_definitions("-Wall -Wextra -Werror")

# Find required packages
find_package(MAVSDK REQUIRED)    # MAVSDK package for drone control
find_package(rclcpp REQUIRED)    # ROS 2 package if you're using ROS nodes

# Specify your app's executable name and list of source files used to create it.
add_executable(drone_control_system
    /home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/control_mavsdk.cpp  # Full path to control_mavsdk.cpp
    #src/control_mavsdk.cpp  # Your main control file
    /home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/engine.c  # Drone Control Engine
    #src/engine.c            # Drone control engine file
    #/home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/v2c.h  # 
    #src/v2c.h               # Header file (not compiled but included in source files)
   #/home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/control.h 
)

# Link against MAVSDK and ROS 2 libraries
target_link_libraries(drone_control_system
    MAVSDK::mavsdk               # Link against MAVSDK core
    MAVSDK::mavsdk_action        # Add the action plugin for controlling the UAV (e.g., takeoff, land, etc.)
    MAVSDK::mavsdk_telemetry     # Add the telemetry plugin to get drone data like position, battery, etc.
    MAVSDK::mavsdk_offboard      # Add offboard plugin for precise position control
    rclcpp                       # Link ROS 2 if you are using ROS nodes in your system
)

# Install the executable
#install(TARGETS drone_control_system DESTINATION lib/${PROJECT_NAME})

# Install the executable
install(TARGETS drone_control_system DESTINATION lib/STAD_mccoychisom)


