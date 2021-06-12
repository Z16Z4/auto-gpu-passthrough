import os, re, display, packages, config

os.system("clear")
def menu():
    #default menu
    display.banner()
    display.sep()
menu()
option = input("user@holy-grail-installer> ")

while option != 0:
    if option == "0":
        #null
        print()
    elif option == "exit":
        #close program
        print("Goodbye")
        exit()
    elif option == 'ls':
        #listing commands
        display.sep()
        display.commands()
    elif option == 'greeks install' or option == '1':
        #installing my packages
        packages.greeks_install()
        config.greek_grub_config()
        file_exists2 = os.path.exists("./configurations/.boot2")
        if file_exists2 == False:
            config.vfio_config()
        elif file_exists2 == True:
            print("Vfio already configured.. skipping step")
        config.greeks_bashrc()
        config.greeks_qemu_config()
        config.greeks_script_setup()
    elif option == '2' or option == 'auto setup':
        #installation of users packages
        packages.users_install()
        #checking if new grub file exists
        file_exists = os.path.exists('./configurations/user_config/grub')
        if file_exists == False:
            #configures grub for amd and intel systems for iommu
            config.grub_config()
        elif file_exists == True:
            print("Grub already configured.. skipping step")
    elif option == "clear" or "3":
        #clear terminal option
        display.clear()
    elif option == "exit":
        #close program
        print("Goodbye!")
        quit()
        exit()
        sys.exit()
    else:
        print("Not a command")
    print()
    #user bar
    option = input("user@holy-grail-installer> ")
