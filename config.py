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
        print("Manual configuration") 
        os.system("sudo cp ./configurations/vfio-pci-override.sh")
    else:
        print("Unknown Entry, Please try again!")
        vfio_config()
    os.system("sudo cp ./configurations/mkinitcpio.conf /etc/")
    os.system("sudo cp ./configurations/vfio.conf /etc/modprobe.d")

def greeks_bashrc():
    os.system("sudo chsh -s /bin/bash")
    os.system("sudo chsh -s /bin/bash greek")
    os.system("sudo cp ./configurations/.bashrc /home/greek")
    

    
