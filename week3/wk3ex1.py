#!/usr/bin/env python
"""
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract
all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list
where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data
structure to the screen. Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
"""
#for backwards compatibility with pyton2
from __future__ import unicode_literals, print_function
#gives us the pretty print so output looks the same as the desired output in description
from pprint import pprint
"""
my way of opening files since VS code tries to execute the python files at the root and not the folder 
they are located in
"""

#initialize vlan_list variable to be used later in a loop
vlan_list = []

from pathlib import Path
data_folder = Path("week3/")
file_to_open = data_folder / "show_vlan.txt"

#opens the file using a with loop
with open(file_to_open) as f:
    sh_vlan = f.read()

#iterates through txt file splitting it up by line
for line in sh_vlan.splitlines():
    #if the line begins with VLAN, -----, or blank space it is passed by the loop to eliminate headers
    if 'VLAN' in line or '-----' in line or line.startswith('  '):
        continue #basically tells the loop to skip ther iterations that match the aobove statment but keep iterating
    #the two lines above remove the headers of the text file, this line splits each line by spaces and puts the contents into the fields variable
    fields = line.split()
    #further splitting up the fields by taking the vlan id which is index 0 of fields variable and stores it in vlan_id variable
    vlan_id = fields[0]
    #further splitting up the fields by taking the vlan name which is index 1 of fields variable and stores it in vlan_name variable
    vlan_name = fields[1]
    #earlier we initialised a blank list variable vlan_list. this is adding the vlan_id and vlan_name as a touple to the list
    vlan_list.append((vlan_id, vlan_name))

#prints a blank line
print()
#pretty print the vlan_list vriable so it shows up the requested way)
pprint(vlan_list)
#prints a blank line
print()