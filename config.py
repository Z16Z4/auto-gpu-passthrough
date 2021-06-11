import os, platform, subprocess, cpuinfo, display
def greek_grub_config():
    os.system("sudo cp ./configurations/greeks_config/grub /etc/default/grub")
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")

def grub_config():
    brand = cpuinfo.cpu.info[0]['vendor_id']
    if brand == 'AuthenticAMD':
        print("This is a amd cpu, adding grub")
        with open('./configurations/greeks_config/grubs/amd/grub', 'r') as rf:
            with open('./configurations/user_config/grub', 'w') as wf:
                for line in rf:
                    wf.write(line)
        os.system("sudo cp ./configurations/user_config/grub /etc/default/grub")
    elif brand == 'GenuineIntel':
        print("This is a intel cpu, adding grub")
        with open('./configurations/greeks_config/grubs/intel/grub', 'r') as rf:
            with open('./configurations/user_config/grub', 'w') as wf:
                for line in rf:
                    wf.write(line)
        os.system("sudo cp ./configurations/user_config/grub /etc/default/grub")
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
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
        #    print(line, end='')
