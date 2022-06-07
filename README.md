# MAV_PROJECT
Creating Build Instructions for Macros &amp; PX4 to be used in a Docker Image

## BUILDING THE PX4 LIBRARY ON DOCKER

STEP #1
In Terminal, navigate to the build directory of your choice and run the command
```
git clone https://github.com/PX4/PX4-Autopilot.git 
```
This will clone the PX4 Autopilot folder into your directory

STEP #2 
From the Docker Image, navigate to ``` catkin_ws/src/course_dir ``` and from there run the bash script
```sudo bash ./Customization.bash```. This will install all necessary libraries required to build PX4 Autopilot. 

STEP #3
Navigate to the newly cloned repo from Step 1, again from the docker image. We will build the project via the command ```no_sim=1 make px4_sitl_defeault gazebo```. This will build all necesary components from the PX4 side.

Step #4
Lastly, we will perform a catkin build on the PX4 package. We run the command ```catkin build px4``` and this will build the ```mav_msgs``` package and the ```px4``` package. Note that this step takes an extremely long time to complete (45 minutes to one hour). 
