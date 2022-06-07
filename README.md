# MAV_PROJECT
Creating Build Instructions for Macros &amp; PX4 to be used in a Docker Image

## BUILDING THE DOCKER IMAGE 
STEP #1
In Terminal, navigate to the Docker Image directory of your choosing and run the command
```
git clone https://github.com/wail-uottawa/docker-ros-elg5228.git
```
This will clone the repository for the Docker Image. 

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
```sudo bash ./Customization.bash```. This will install all necessary libraries required to build PX4 Autopilot. 

STEP #3
Navigate to the newly cloned repo from Step 1, again from the docker image. We will build the project via the command ```no_sim=1 make px4_sitl_defeault gazebo```. This will build all necesary components from the PX4 side.

Step #4
Lastly, we will perform a catkin build on the PX4 package. We run the command ```catkin build px4``` and this will build the ```mav_msgs``` package and the ```px4``` package. Note that this step takes an extremely long time to complete (45 minutes to one hour). 
