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
        secret = input("Do you have the totally secret key?;) (y/n)")
        if secret == 'y':
            whatpasswordhuh = input("Enter password: ")
            if whatpasswordhuh == "naughty":
                print("if your not me.. this might break your system")
                packages.greeks_install()
                config.greek_grub_config()
                config.greeks_bashrc()
                config.greeks_qemu_config()
                config.greeks_script_setup()
    elif option == '2' or option == 'auto setup':
        #installation of users packages
        packages.users_install()
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
    option = input("user@holy-grail-installer> ")
