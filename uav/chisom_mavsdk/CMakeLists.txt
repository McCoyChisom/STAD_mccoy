cmake_minimum_required(VERSION 3.15)

# Specify your project's name
project(control_mavsdk)

# Specify at least C++11, better C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Enable strict handling of warnings
add_definitions("-Wall -Wextra -Werror")

# Finds MAVSDK when installed system wide.
find_package(MAVSDK REQUIRED)

# Specify your app's executable name, and list of source files used to create it.
#add_executable(test
#    control_mavsdk.cpp
    # ... any other source files
    #)
    
# Specify your app's executable name and list of source files used to create it.
add_executable(control_mavsdk
    /home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/control_mavsdk.cpp  # Full path to control_mavsdk.cpp
    #src/control_mavsdk.cpp  # Your main control file
    /home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/engine.c  # Drone Control Engine
    #src/engine.c            # Drone control engine file
    #/home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/v2c.h  # 
    #src/v2c.h               # Header file (not compiled but included in source files)
   #/home/mccoychisom/STAD_mccoychisom/uav/control/chisom_mavsdk/src/control.h 
)


add_library(control_mavsdk SHARED control_mavsdk.cpp)

target_include_directories(control_mavsdk PRIVATE .)

# Specify your app's executable name and a list of linked libraries
target_link_libraries(control_mavsdk
     MAVSDK::mavsdk               	# All apps link against mavsdk library
     # MAVSDK::mavsdk_action      	# If action plugin used by app ...
     # MAVSDK::mavsdk_telemetry   	# If telemetry plugin used by app ...
     # MAVSDK::offboard
     # ... Any other linked libraries
)
