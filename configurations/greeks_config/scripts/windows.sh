#!/bin/bash
sudo mount /dev/sda1 /home/greek/media/iso
sudo virsh start win10
#synergyc -f --daemon 192.168.122.57:24804
scream -i virbr0 &
looking-glass-client -F opengl:vsync input:rawMouse
