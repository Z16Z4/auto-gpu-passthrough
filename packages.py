import os


def users_install():
    #hoil grail packages
    print("iptables-nft is optional and may break some setups")
    os.system("sudo pacman -S iptables-nft")
    os.system("sudo pacman -S qemu libvirt edk2-ovmf virt-manager dnsmasq")

