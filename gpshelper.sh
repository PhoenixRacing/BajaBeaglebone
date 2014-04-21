#!/bin/bash
echo T8LO-GPS > /sys/devices/bone_capemgr.*/slots 
gpsd -F /var/run/gpsd.sock /dev/ttyO4
