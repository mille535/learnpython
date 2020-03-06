#!/usr/bin/env python
#^shebang, allows direct execution on *nix and mac
#imports future to allow compatibility with python2
from __future__ import print_function

#importing example variable
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

#splitting sh ver output and getting 2nd field for model number
model_no = show_version.split()[1]
#splitting sh ver output and getting 3rd field for serial number
serial_no = show_version.split()[2]
#check to see if the string cisco is in the model number without case sensitivity
is_cisco = "cisco" in model_no.casefold()
#check to see if 881 is in the model string
is_881 = "881" in model_no
#prints the show version without leading and tailing spaces
print(show_version.strip())
#prints sh version info split out
print(show_version.split())
#prints model number
print(f"Model number is: {model_no}")
#prints serial number
print(f"Serial number is: {serial_no}")
#prints whether cisco is in the model number
print(f"Is Cisco in the model number? {is_cisco}")
#prints whether or not this is an 881
print(f"Is this a Cisco 881? {is_881}")

