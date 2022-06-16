# Place this file in the drive that is mapped to your local computer
# e.g., drive "course_dir"
# This file is sourced automatically by .bashrc
# It allows further customization if needed without rebuilding the image

# See the following link for some examples of Husky customization
# environment variables
# http://wiki.ros.org/husky_bringup/Tutorials/Customize%20Husky%20Configuration

# Enable the SICK LMS1XX LIDAR on Husky
export HUSKY_LMS1XX_ENABLED=true
export PYTHONPATH=.
pip3 install kconfiglib
pip3 install empy
pip3 install jsonschema 
pip3 install pyros_genmsg 
pip3 install toml 
pip3 install numpy 
pip3 install future 
sudo -S apt-get install libgstreamer1.0-dev 
sudo -S apt-get install libgstreamer-plugins-base1.0-dev 
sudo -S apt-get install libgstreamer-plugins-bad1.0-dev 
sudo -S apt-get gstreamer1.0-plugins-base 
sudo -S gstreamer1.0-plugins-good  
sudo -S apt-get gstreamer1.0-plugins-bad  
sudo -S apt-get install gstreamer1.0-plugins-ugly  
sudo -S apt-get install gstreamer1.0-libav gstreamer1.0-doc 
sudo -S apt-get install gstreamer1.0-tools gstreamer1.0-x 
sudo -S apt-get install gstreamer1.0-alsa gstreamer1.0-gl 
sudo -S apt-get install gstreamer1.0-gtk3 
sudo -S apt-get install gstreamer1.0-qt5 
sudo -S apt-get install gstreamer1.0-pulseaudio 