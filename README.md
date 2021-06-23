
NVIDIA LINUX, JETPACK, DEEPSTREAM FLASH INSTALL
===============================================

# flash linux for tegra (L4T) onto bootable SD card
https://developer.nvidia.com/jetson-nx-developer-kit-sd-card-image

# jetpack
sudo apt update
sudo apt install nvidia-jetpack

# deepstream

https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Quickstart.html
https://developer.nvidia.com/deepstream-getting-started

UBUNTU LINUX
============
# set window menus to app
settings/appearance/bind 

DEEPSTREAM
==========
# link  to deepstream sample configs
ln -s /opt/nvidia/deepstream/deepstream/samples/configs/deepstream-app/  ~/

DEPENDENCIES
============
# utility for device resolution
sudo apt install v4l-utils

v4l2-ctl --list-devices
v4l2-ctl -d /dev/video0 --list-formats-ext

MICROSOFT VSCODE
================
https://code.visualstudio.com/download
cd ~/Downloads
sudo apt install ./code_1.57.1-1623936438_arm64.deb
code

# install python

GITHUB
======
# open repository from vscode
prompt for repository: https://github.com/culebracut/robo2
prompt for location ~/workspace/robo2

TESTING
=======
# display usb webcam on video1 : fakesync and monitor
gst-launch-1.0 v4l2src ! xvimagesink
gst-launch-1.0 -v v4l2src device=/dev/video1 ! fakesink
gst-launch-1.0 -v v4l2src device=/dev/video1 ! xvimagesink
# display csi camera on monitor
gst-launch-1.0 nvarguscamerasrc sensor-id=0 ! 'video/x-raw(memory:NVMM), width=640, height=540,format=NV12, framerate=30/1' ! nvoverlaysink -e

RESOURCES
=========
GSTREAMER https://developer.download.nvidia.com/embedded/L4T/r32_Release_v1.0/Docs/Accelerated_GStreamer_User_Guide.pdf

RUNTIME
=======
# test deepstream with file usb, csi camera.  
cd ~/myapps
# CSI camera on /dev/video0
deepstream-app -c mycsi.txt
# USB camera on /dev/video1
#
install pip

GITHUB ROBO
===========
# set git permissions
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# python code for robot
git clone https://github.com/culebracut/robo2.git


