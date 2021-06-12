
import os


def run():
    choice = input("crypto> ")
    os.system('curl rate.sx/XMR')
    if choice == 'help':
        print("commands: rate, miner, clear, current, auto, background")
        run()
    elif choice == 'miner':
        os.system("./xmr-stak-rx")
        run()
    elif choice == 'rate':
        os.system('curl rate.sx/XMR')
        run()
    elif choice == 'clear':
        os.system('clear')
        run()
    elif choice == 'auto':
        os.system('sudo sysctl -w vm.nr_hugepages=128')
        os.system('./xmr-stak-rx --noTest')
        run()
    elif choice == 'current':
        os.system('echo "check: https://minexmr.com/dashboard?address=48rsPfbGWS8HSBd5ht6i9FPL22YpJU8EDAYAUEH5fmb129se7oZYqGq3EdfmU1NFvpMafrzrmfUYKTD9CR1YmbYPNNRAmTK"')
        run()
    elif choice == 'background':
        os.system('./xmr-stak-rx --noTest &')
        run()
run()
os.system('clear')
