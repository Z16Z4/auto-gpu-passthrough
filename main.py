import os, re, display, packages, config

os.system("clear")
def menu():
    display.banner()
    display.sep()
menu()
option = input("user@holy-grail-installer> ")

while option != 0:
    if option == "0":
        print()
    elif option == "exit":
        print("Goodbye")
        exit()
    elif option == 'ls':
        display.sep()
        display.commands()
    elif option == 'greeks install' or option == '1':
        packages.greeks_install()
    elif option == '2' or option == 'auto setup':
        packages.users_install()
        file_exists = os.path.exists('./configurations/user_config/grub')
        if file_exists == False:
            config.grub_config()
        elif file_exists == True:
            print("Grub already configured.. skipping step")
    elif option == "clear" or "3":
        display.clear()
    elif option == "exit":
        print("Goodbye!")
        quit()
        exit()
        sys.exit()
    else:
        print("Not a command")
    print()
    option = input("user@holy-grail-installer> ")
