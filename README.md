CREATE BOOTABLE SD CARD
=======================

DOWNLOAD FOR JETSON NX
======================
https://developer.nvidia.com/jetson-nx-developer-kit-sd-card-image

DOWNLOAD FOR JETSON NANO
========================
???

FLASH LINUX FOR TEGRA ONTO BOOTABLE SD CARD
===========================================
https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit

BOOT INTO UBUNTU LINUX
======================
# set window menus to app
settings/appearance/bind 

# set cpu clock and fan to max
$ sudo nvpmodel -m 0
$ sudo jetson_clocks

JETPACK
=======
sudo apt update
sudo apt install nvidia-jetpack

DEEPSTREAM
==========
# download DS and install
https://developer.nvidia.com/deepstream-getting-started
cd ~/Downloads
sudo apt-get install ./deepstream-5.1_5.1.0-1_arm64.deb
# link  to deepstream sample configs
ln -s /opt/nvidia/deepstream/deepstream/samples/configs/deepstream-app/  ~/myapps
cd ~/myapps
deepstream-app -c source1_usb_dec_infer_resnet_int8.txt

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

PIP
===
sudo apt install python3-pip
pip3 list

UTILS
=====
sudo pip3 install jetson-stats
sudo jtop
# set fan speed.  note temperature difference.

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


