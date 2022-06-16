# MAV_PROJECT
Creating Build Instructions for Macros &amp; PX4 to be used in a Docker Image

## BUILDING THE DOCKER IMAGE 
STEP #1
In Terminal, navigate to the Docker Image directory of your choosing and run the command
```
git clone https://github.com/wail-uottawa/docker-ros-elg5228.git
```
This will clone the repository for the Docker Image. Note that the root password for any ```sudo``` command is 'ros' (no quotation marks)

STEP #2
Modify the file
```
docker-run.sh
```
Such that the course directory is mapped to a directory of your choosing on your remote system. 

STEP #3

Replace the ```customization.bash``` 
script with the one located in this repository. This will allow you to install more packages related to PX4 on the Docker Image.

STEP #4
With Docker Desktop Downloaded, run the 
```
docker-run.sh
```
script and the image should be pulled from Docker and then ran. You may use TigerVNC Viewer (password: vncpassword) to obtain a GUI representation.


## BUILDING THE PX4 LIBRARY ON DOCKER

STEP #1
In Terminal, navigate to the build directory of your choice and run the command
```
git clone https://github.com/PX4/PX4-Autopilot.git 
```
This will clone the PX4 Autopilot folder into your directory

STEP #2 
From the Docker Image, navigate to ``` catkin_ws/src/course_dir ``` and from there run the bash script
```sudo bash ./customization.bash```. This will install all necessary libraries required to build PX4 Autopilot. 

STEP #3
Navigate to the newly cloned repo from Step 1, again from the docker image. We will build the project via the command ```no_sim=1 make px4_sitl_defeault gazebo```. This will build all necesary components from the PX4 side.

Step #4
Lastly, we will perform a catkin build on the PX4 package. We run the command ```catkin build px4``` and this will build the ```mav_msgs``` package and the ```px4``` package. Note that this step takes an extremely long time to complete (45 minutes to one hour). 

## BUILDING MAVROS 

STEP #1
In order to use the MAVROS API we must first install the Geoids library. In order to do this, navigate to ```cd /opt/ros/melodic/lib/mavros``` and then install the Geoids Library via ```sudo bash ./install_geographiclib_datasets.sh```

## RUNNING MAVROS

STEP #1
In order to run MAVROS (with PX4), we enter the command ```roslaunch mavros px4.launch fcu_url:="//udp://:14540@127.0.0.1:14557"```. What this means is that the Virtual Ground Control station (MAVROS) is listening on the localhost IP 127.0.0.1 on port 14557, while the PX4 connection accepts the connection on port 14540.

## BUILDING VELOCITY CONTROLLER

STEP #1 
Navigate to the catkin_ws directory on the docker image. Call the command ```catkin build velocitycontroller rospy geometry_msgs```to build the ros package.

STEP #2
The velocity controller can now be run using ```rosrun velocitycontroller getuserinputpy.py``` and in a seperate terminal ```rosrun velocitycontroller publishheartbeat.py```. The publisher publishes the last known state of the user input. Press w or a to controll the drone's y velocity, press a or d to control the x velocity and press space bar or v to controll the drone's z velocity. To get the drone to hover, press 'x'.

## RUNNING PX4

STEP #1 
We first wish to configure the path to the URDF Quadcopter models. First navigate to the cloned PX4-Autopilot repository, and run the command ```source Tools/setup_gazebo.bash $(pwd) $(pwd)/build/sitl_default```. If the URDF models are still not detected during execution, you may have to truncate the .jinja extension on these models.

STEP #2 
For convenience, we wish to add PX4 to the Ros Package Path. Do this by running ```export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)``` followed by ```export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools_sitl_gazebo 

STEP #3
We now can launch PX4 by calling the command ```roslaunch px4 posix_sitl.launch```. Note that this should be done after setting up the MAVROS process. 
In a seperate terminal window, verify that the MAV is connected via MAVROS by calling the command ```rostopic echo mavros/state```. If the state reads ```AUTO.LOITER``` then the connection is succesful. However, if the state is read as '', then try running steps #1-#3 of this section. 

STEP #4
We now wish to enable ```OFFBOARD``` mode for the IRIS Drone. The first failsafe must be disabled. We first change parameter ```COM_RLL_EXCEPT``` to '4' via the command ```rosservice call mavros/param/set "{'param_id':'COM_RLL_EXCEPT', 'value':[4, 0]}"

STEP #5
We now wish to disable the second failsafe parameter. In order to do this, we change parameter ```NAV_RCL_ACT```to 0. Run the command ```rosservice call mavros/param/set "{'param_id':'NAV_RCL_ACT', 'value':[0, 0]}"

STEP #6 
In order to enable the ```OFFBOARD``` mode for the IRIS Drone, we must pass either a position or velocity command in order to enable triggering a failsafe. 
Run the pose publishing program 

