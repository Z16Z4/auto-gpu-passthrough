
import os


def banner():
    print("--------------------------------------")
    print("  _        _                      _ _ ")
    print(" | |_  ___| |_  _   __ _ _ _ __ _(_) |")
    print(" | ' \/ _ \ | || | / _` | '_/ _` | | |")
    print(" |_||_\___/_|\_, | \__, |_| \__,_|_|_|")
    print("             |__/  |___/              ")
    print("--------------------------------------")
    print("                                      ")
    print(" Enter 'ls' to get going")


def sep():
    print("                                      ")



def commands():
    print("Commands:")
    print("---------")
    print("1. greeks install - Installer designed for my system")
    print("2. auto setup    -  Your installer                  ")
    print("3. clear - clear terminal                           ")
    sep()
    print("Enter 'exit' to close program                       ")


def clear():
    os.system("clear")


def reboot_menu():
    print("Please reboot system and rerun scripts!")
    reboot = input("reboot now? (y/n): ")
    if reboot == 'y' or reboot == 'yes':
        os.system("sudo shutdown -r now")
    elif reboot == 'n' or reboot == 'no':
        print("you gotta remember then!")
        quit()
    else:
        print("Invalid option")
        reboot_menu()