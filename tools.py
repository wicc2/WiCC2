#!/usr/bin/env python3
import os
import urllib.request

os.close(2)

# check root privilege
if os.getuid() != 0:
    print("Error: script must be executed as root\n")
    exit(1)

print("Creating shortcut...")

cur_dir = os.path.realpath(__file__)[:-len("tools.py")]
print("Current directory: " + cur_dir)

bin_dir = os.path.defpath.split(":")[2]
print("OS bin directory: " + bin_dir)

link_cmd = "ln -s " + cur_dir + "WiCC.py " + bin_dir + "/wicc"

out = os.system(link_cmd)
if out > 0:
    print("Error creating symbolic link")
else:
    print("Created symbolic link, use:\n\twicc\nto execute the program (with root privileges)")

print("\n----------------------------------")
print("Installing all necesary software:\n")

os.system("dpkg --configure -a")
out = os.system("apt-get install --yes python3 python3-tk iw net-tools aircrack-ng "
                "gcc make libpcap-dev libssl-dev pyrit crunch")
print("\ninstalling cowpatty")
urllib.request.urlretrieve("http://pkgs.fedoraproject.org/repo/pkgs/cowpatty/cowpatty-4.6.tgz/"
                                   "b90fd36ad987c99e7cc1d2a05a565cbd/cowpatty-4.6.tgz", "cowpatty-4.6.tgz")
os.system("tar xvzf cowpatty-4.6.tgz")
print("Cowpatty downloaded and extracted, making...")
print("\n----------------------------------")

if out == 0:
    print("All software installed correctly")
else:
    print("Some installation failed, please try running the installer again")
