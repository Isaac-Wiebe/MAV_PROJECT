#!/bin/sh

docker run -it --rm --privileged --name docker-ros-elg5228 \
       -p 5901:5901 \
       -p 6901:6901 \
       --volume ~/Documents/GraduateStudies/MobileRobots:/home/ros/catkin_ws/src/course_dir \
       realjsk/docker-ros-elg5228:20210908 \
       bash

