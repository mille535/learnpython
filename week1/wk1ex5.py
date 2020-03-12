#!/usr/bin/enf python
from __future__ import print_function, unicode_literals

#prefefined variables mac table
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

#my cunning additions
mac1_fields = mac1.split()
mac2_fields = mac2.split()
mac3_fields = mac3.split()
#commence the printing of shit
print("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print("-" * 40)
print("{:>20}{:>20}".format(mac1_fields[1], mac1_fields[3]))
print("{:>20}{:>20}".format(mac2_fields[1], mac2_fields[3]))
print("{:>20}{:>20}".format(mac3_fields[1], mac3_fields[3]))
print("-" * 40)
print("\n")
