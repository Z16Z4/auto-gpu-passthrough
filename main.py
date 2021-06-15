import os, re, display, packages, config

os.system("clear")
def menu():
    #default menu
    display.banner()
    display.sep()
menu()
option = input("user@auto-gpu-passthrough> ")
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
        print("Invalid option please download https://github.com/cronos-hash/myconf")
    elif option == '2' or option == 'auto setup':
        packages.userinstall()
        file_exists = os.path.exists('./configurations/user_config/ran_install_before')
        if file_exists == True:
            print("Setuop has ran before, replacing kernel configuration template")
            os.system("sudo rm ./configurations/user_config/ran_install_before")
            os.system("sudo rm ./configurations/user_config/mkinitcpio.conf")
            os.system("sudo cp ./configurations/user_config/backup/mkinitcpio.conf ./configurations/user_config/mkinitcpio.conf")
            config.grub_config()
            config.vfio_config()
        elif file_exists == False:
            packages.userinstall()
            config.grub_config()
            config.vfio_config()
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
    option = input("user@auto-gpu-passthrough> ")
