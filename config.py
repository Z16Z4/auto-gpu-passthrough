import os, platform, subprocess, cpuinfo, display, re
def greek_grub_config():
    #copy over my configurations 
    os.system("sudo cp ./configurations/greeks_config/grubs/amd/grub /etc/default/grub")
    #rebuild grub bootloader
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")

#Function for creating grub configuration depending on the users cpu vendor, this will enable iommu
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

       
def vfio_config():
    #asks the user to select either manual mode or automatic mode for their gpu
    gpu_passthrough = input("Manually Select GPU or Automatic mode? (man/auto)")
    #if they select auto mode then a different script will be used on the system to passthrough the gpu which isnt being used as the main gpu currently
    if gpu_passthrough == "auto":
        print("Auto configuration")
    #however, if the user selects manual mode then it will edit a script with the device id of the gpu that the user selects
    elif gpu_passthrough == "man":
        #opening/creating iommu pairs file
        with open('./configurations/user_config/iommu_pairs', 'w') as man:
            #storing devices that match as a "VGA" device by filtering the lspci command with the keyword "VGA"
            output = os.popen("lspci -nnk | grep 'VGA'").read()
            #seeking the beginning of the file
            man.seek(0)
            #writing the output of the linux command (the graphic cards to the file)
            man.writelines(str(output))
        #executing vfio menu to set up the device
        vfio_menu()
    else:
        #if the user enters something wrong it will then recall this function
        print("Unknown Entry, Please try again!")
        vfio_config()
    display.reboot_menu()

def vfio_menu():
    #default array of devices
    devices = []
    #opening iommu_pairs file which has the gpu devices saved
    with open("./configurations/user_config/iommu_pairs", 'r') as manr:
        #enumerating this file, so the user can select these devices from a menu
        for index, line in enumerate(manr):
            #adding these devices to an array to get their device id 
            devices.append(line)
            #printing these devices for the user to select
            print("Enter " + str(index) + " for : \n", line)
            #getting users input of the number choosen correlating to the gpu they selected
        Select_GPU = input("Please select the GPU for passthrough using the numbers above?: ")
        #opening device_ids file 
        with open("./configurations/user_config/device_ids", 'w') as gputemp:
            #the selected device, is the device in the array matching the index
            selected_device = devices[int(Select_GPU)]
            #the true device id is filtered unneeded information about the GPU
            device_id = re.split("\s", devices[int(Select_GPU)])
            #the device id of the gpu also correlates with the audio device within the gpu
            #in most cases this device id shares the same id but 1 from root
            device_audio = ''.join(str(device_id[0]))
            #replacing unneeded part of device id for device audio id 
            device_audio = device_audio.replace(".0","")
            #this would give the full address to the device id
            #for example "0000:08:00.0 0000:08:00.1"
            gputemp.writelines("0000:" + device_id[0] + " " + "0000:" + device_audio + ".1")
            #same occurance however used for modifying the vfio pci override
            full_device = "0000:" + device_id[0] + " " + "0000:" + device_audio + ".1"
            override_data = ''.join(str(full_device))
            print("You have choosen " + str(selected_device))
        with open("./configurations/user_config/manual/vfio-pci-override.sh", 'r') as vfio_script:
            #reading lines from vfio-pci-override script
            override = vfio_script.readlines()
            #replacing device id within this script 
            override[2] = 'DEVS="' + override_data + '"\n' 
        with open("./configurations/user_config/manual/vfio-pci-override.sh", 'w') as vfio_script:
            #writing the device id to the file
            vfio_script.writelines(override)
    mkinitcpio_manual_config()
        
def mkinitcpio_manual_config():
    print("warning: about to change your kernel configurations!!")
    configurekernel = input("would you like to proceed? (y/n)")
    if configurekernel == 'y':
        amdgpu = input("are you using a amdgpu for your main unvritualised display? (y/n)")
        if amdgpu == 'y':
            os.system("sudo cp ./configurations/user_config/20-amdgpu.conf /usr/share/X11/xorg.conf.d")
            with open("./configurations/user_config/mkinitcpio.conf", 'r') as mkinitcpio:
                mconf = mkinitcpio.readlines()
                mconf[9] = "MODULES=(vfio_pci vfio vfio_iommu_type1 vfio_virqfd amdgpu radeon)"
            with open("./configurations/user_config/mkinitcpio.conf", 'w') as mkinitcpio:
                mkinitcpio.writelines(mconf)
        elif amdgpu == 'n':
            print("okie, got it !")
            with open("./configurations/user_config/mkinitcpio.conf", 'r') as mkinitcpio:
                mconf = mkinitcpio.readlines()
                mconf[9] = "MODULES=(vfio_pci vfio vfio_iommu_type1 vfio_virqfd) \n"
            with open("./configurations/user_config/mkinitcpio.conf", 'w') as mkinitcpio:
                mkinitcpio.writelines(mconf)
        else:
            print("wrong selection, please try again!")
            mkinitcpio_manual_config()
    elif configurekernel == 'n':
        exit()
    else:
        print("Invalid entry")
    with open("./configurations/user_config/mkinitcpio.conf", 'r') as mkinitcpio:
        mconf = mkinitcpio.readlines()
        mconf[21] = 'FILES="/usr/local/bin/vfio-pci-override.sh" \n'
    with open("./configurations/user_config/mkinitcpio.conf", 'w') as mkinitcpio:
        mkinitcpio.writelines(mconf)
    os.system("sudo chmod +x ./configurations/user_config/manual/vfio-pci-override.sh")
    os.system("sudo cp ./configurations/user_config/manual/vfio-pci-override.sh /usr/local/bin")
    os.system("sudo cp ./configurations/user_config/mkinitcpio.conf /etc/")
    os.system("sudo cp ./configurations/user_config/vfio.conf /etc/modprobe.d")
    os.system("sudo mkinitcpio -p linux")
    display.reboot_menu()
    #creating a hidden file, so that when the installer is reran the program knows due to the existence of this file 
    #UNCOMMENTos.system("touch ./configurations/.boot2")
def greeks_bashrc():
    os.system("sudo chsh -s /bin/bash")
    os.system("sudo chsh -s /bin/bash greek")
    os.system("sudo cp ./configurations/greeks_config/.bashrc /home/greek")

def greeks_qemu_config():
    os.system("sudo cp ./configurations/greeks_config/vfio-pci-override.sh /usr/local/bin")
    os.system("sudo cp ./configurations/greeks_config/mkinitcpio.conf /etc/")
    os.system("sudo cp ./configurations/greeks_config/vfio.conf /etc/modprobe.d")
    os.system("sudo mkinitcpio -p linux")
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
    os.system("sudo cp ./configurations/greeks_config/virt-manager/OVMF_VARS-1024x768.fd /home/greek/media/iso/macOS-Simple-KVM/firmware/OVMF_VARS-1024x768.fd")
    os.system("mkdir /home/greek/miner")
    os.system("sudo cp ./configurations/greeks_config/miner/* /home/greek/miner")
    os.system("sudo cp ./configurations/greeks_config/rc.xml /home/greek/.config/openbox")
    os.system("openbox --restart")
    os.system("sudo cp ./configurations/greeks_config/10-looking-glass.conf /etc/tmpfiles.d")
    os.system("sudo cp ./configurations/greeks_config/20-amdgpu.conf /usr/share/X11/xorg.conf.d")
    os.system("sudo chmod +x ./configurations/greeks_config/install_others.sh")
    print("please run additional script for looking glass etc! (cant run as sudo)")
    display.reboot_menu()
    
