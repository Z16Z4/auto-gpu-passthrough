import os

def greeks_install():
    os.system("sudo pacman -S cool-retro-term net-tools git firefox discord barrier synergy cmatrix bashtop youtube-dl figlet neofetch lolcat tmux exa bat starship task")
    os.system("sudo pacman -S qemu libvirt edk2-ovmf virt-manager iptables-nft dnsmasq")

def users_install():
    os.system("sudo pacman -S qemu libvirt edk2-ovmf virt-manager iptables-nft dnsmasq")

