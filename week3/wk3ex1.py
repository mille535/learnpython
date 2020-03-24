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
from __future__ import unicode_literals, print_function

"""
my way of opening files since VS code tries to execute the python files at the root and not the folder 
they are located in
"""
from pathlib import Path
data_folder = Path("week3/")
file_to_open = data_folder / "show_vlan.txt"

with open(file_to_open) as f:
    sh_vlan = f.read()

print(sh_vlan.splitlines())