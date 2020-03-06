#!/usr/bin/env python
#^shebang, allows direct execution on *nix and mac
#imports future to allow compatibility with python2
from __future__ import print_function

#prompt user for input trying it in either python3 or python2 format
try:
    ip_addr = raw_input("Enter an IP Address: ")
except NameError:
    ip_addr = input("Enter an IP address: ")

#define variable breaking out decimal octets of ip_addr
dec_octets = ip_addr.split('.')
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
#prints out the decimal version of the octets, the easy way.
print("{:^15}{:^15}{:^15}{:^15}".format(*dec_octets))
#prints out the binary version of the octets converting eatch part of the list to an integer and then to binary
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(dec_octets[0])), bin(int(dec_octets[1])), bin(int(dec_octets[2])), bin(int(dec_octets[3]))))
#prints out the hex version of the octets converting each part of the list to an integer and then to hex
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(dec_octets[0])), hex(int(dec_octets[1])), hex(int(dec_octets[2])), hex(int(dec_octets[3]))))
print("-" * 60)
