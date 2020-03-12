#!/usr/bin/env python
from __future__ import print_function, unicode_literals
"""Read in the "show_ip_int_brief.txt" file into your program using the
.readlines() method.
Obtain the list entry associated with the FastEthernet4 interface. You can
just hard-code the index at this point since we haven't covered for-loops
or regular expressions:
Use the string .split() method to obtain both the IP address and the
corresponding interface associated with the IP.
Create a two element tuple from the result (intf_name, ip_address).
Print that tuple to the screen.
Use pycodestyle on this script. Get the warnings/errors to zero. You might need
to 'pip install pycodestyle' on your computer (should be able to type this from
the shell prompt). Alternatively, you can type:
  'python -m pip install pycodestyle'.
"""
#opens file with using proper while methed f variable is filename and ip_int is the readlines output to list
with open("show_ip_int_brief.txt") as f:
    ip_int = f.readlines()

#seperating the line for interface fa/4
int_f4 = ip_int[5]
#creats touple variable names int_and_ip_t by splitting the correspoding fields of int_f4 variable
int_and_ip_t = (int_f4.split()[0], int_f4.split()[1])

#prints output
print(int_and_ip_t)

#blank line at the end to make pycodestyle happt even though it angers me
