import os, platform, subprocess, cpuinfo, display
def greek_grub_config():
    #copy over my configurations 
    os.system("sudo cp ./configurations/greeks_config/grubs/amd/grub /etc/default/grub")
    #rebuild grub bootloader
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")

def grub_config():
    #get vendor id of cpu 
    brand = cpuinfo.cpu.info[0]['vendor_id']
    #if the vendor is amd
    if brand == 'AuthenticAMD':
        print("This is a amd cpu, adding grub")
        #open my configuration and a readfile
        with open('./configurations/greeks_config/grubs/amd/grub', 'r') as rf:
            #and then write my readfile configurations to a new file
            with open('./configurations/user_config/grub', 'w') as wf:
                for line in rf:
                    #writes to file
                    wf.write(line)
        #then copy this configuration to grub directory
        os.system("sudo cp ./configurations/user_config/grub /etc/default/grub")
    #however if the cpu is intel vendor
    elif brand == 'GenuineIntel':
        print("This is a intel cpu, adding grub")
        #then read the intel version of the file
        with open('./configurations/greeks_config/grubs/intel/grub', 'r') as rf:
            #and write this to the users configuration directory
            with open('./configurations/user_config/grub', 'w') as wf:
                for line in rf:
                    #writes to file
                    wf.write(line)
        #then copy the configuration to grub directory
        os.system("sudo cp ./configurations/user_config/grub /etc/default/grub")
    #then install the new grub configurations 
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
    #reboot option menu
    display.reboot_menu()
       # f.seek(0) #goes to first line in file (good for writing)
      # f.write('Test') #write to file
      #  f_contents = f.read() #reads whole file
      #  print(f_contents, end='')

        #can read a certain amount of a file using:
        #f_contents = f.read(100)
        #print(f_contents, end='')

        #readfile by line and print with no strange characters
       # for line in f:
       
def vfio_config():
    gpu_passthrough = input("Manually Select GPU or Automatic mode? (man/auto)")
    if gpu_passthrough == "auto":
        #delete manual script, place auto script for gpu
        print("Auto configuration")
    elif gpu_passthrough == "man":
        #menu to select GPU, adds device ID to script
        #write device ids to file
        #display devices for user 
        #number devices
        #if user enters 1 then device 1
        print("Manual configuration") 
        os.system("sudo cp ./configurations/greeks_config/vfio-pci-override.sh")
    else:
        print("Unknown Entry, Please try again!")
        vfio_config()
    os.system("sudo cp ./configurations/greeks_config/mkinitcpio.conf /etc/")
    os.system("sudo cp ./configurations/greeks_config/vfio.conf /etc/modprobe.d")
    os.system("sudo mkinitcpio -p linux")
    os.system("touch ./configurations/.boot2")
    display.reboot_menu()

def greeks_bashrc():
    os.system("sudo chsh -s /bin/bash")
    os.system("sudo chsh -s /bin/bash greek")
    os.system("sudo cp ./configurations/greeks_config/.bashrc /home/greek")

def greeks_qemu_config():
    os.system("sudo pacman -Syu")

    #creating mount point 
    os.system("mkdir /home/media")
    os.system("mkdir /home/media/iso")
    os.system("sudo mount /dev/sda1 /home/greek/media/iso")

    #moving qemu configuration
    os.system("sudo cp ./configurations/greeks_config/qemu.conf /etc/libvirt")

    #starting libvirtd services and log/network
    os.system("sudo systemctl enable libvirtd.service")
    os.system("sudo systemctl start libvirtd.service")
    os.system("sudo systemctl start virtlogd.socket")
    os.system("sudo systemctl virtlogd.socket")
    os.system("sudo virsh net-start default")
    os.system("sudo sudo systemctl restart libvirtd")
    os.system("sudo virsh net-autostart default")


    #defining virt-manager configurations
    os.system("sudo virsh define ./configurations/greeks_config/virt-manager/win10.xml")
    os.system("sudo virsh define ./configurations/greeks_config/virt-manager/macOS.xml")

def greeks_script_setup():
    os.system("mkdir /home/greek/scripts")
    os.system("sudo cp ./configurations/greeks_config/scripts/* /home/greek/scripts")
    os.system("sudo cp ./configurations/greeks_config/virt-manager/OVMF_VARS-1024x768.fd /home/greek/media/macOS-Simple-KVM/firmware/OVMF_VARS-1024x768.fd")
    os.system("mkdir /home/greek/miner")
    os.system("sudo cp ./configurations/greeks_config/miner/* /home/greek/miner")
    os.system("sudo cp ./configurations/greeks_config/rc.xml /home/greek/.config/openbox")
    os.system("openbox --restart")
    os.system("sudo cp ./configurations/greeks_config/10-looking-glass.conf /etc/tmpfiles.d")
    os.system("sudo cp ./configurations/greeks_config/20-amdgpu.conf /usr/share/X11/xorg.conf.d")
    os.system("yay -S looking-glass")
    os.system("yay -S scream")
    display.reboot_menu()
    
