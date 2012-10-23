===========
MoistureCosm
===========

:Author: flexmox@gmail.com

Introduction
============

This is a set of scripts used to upload moisture readings to Cosm/Pachube.  

Installation
============

1. Install moisture sensor (http://www.seeedstudio.com/depot/grove-moisture-sensor-p-955.html?cPath=144_147)
2. Connect to arduino type device (http://arduino.cc/) using 3.3v/5v, GND, and analog input.  In my code I'm using A0.
3. Upload sketch file (moisture_v1.ino) to arduino.
4. Install python dependencies:
  a. PySerial - http://pyserial.sourceforge.net/
  b. Python eeml - https://github.com/flexmox/python-eeml
5. Modify pushtocosm.py to include your personal API and feed number (https://cosm.com)
6. Run python script pushtocosm.py
7. (optional) Set up cron job to run python script at desired interval.


Requirements
============

 * python-eeml
 * PySerial
 * Cosm Account
 * Arduino or any microcontroller able to put out 3.3-5v and connect to a virtual serial port.
 * Moisture sensor

.. _eeml: http://www.eeml.org/
