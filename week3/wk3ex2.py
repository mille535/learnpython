#!/usr/bin/env python
"""
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this
file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a
separate variable.
Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the
string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.
Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then
print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.
Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have
found both of these devices, 'break' out of the for loop.
"""
from __future__ import unicode_literals, print_function
#opens file, additinal stuff for vs code
from pathlib import Path
data_folder = Path("week3/")
file_to_open = data_folder / "show_arp.txt"

#reads file into show_arp variable
with open(file_to_open) as f:
    show_arp = f.read()

#prints a blank line
print()

#define variables for if found sets to false
found1, found2 = (False, False)

#loops though lines (using .splitlines()) of file
for line in show_arp.splitlines():
    #this skips a line if it begins with protocol (note that the line is set to lowercase for better search)
    if 'protocol' in line.lower():
        #continue skips that iteration and moves on
        continue
    
    #breks line variable into individual fiels 
    fields = line.split()
    
    #sets ip_addr vriable to 1st index of fields variable defined above
    ip_addr = fields[1]
    
    #sets mac_addr vriable to 1st index of fields variable defined above
    mac_addr = fields[3]

    #finds ip address 10.220.22.1, prints that its found, and sets found1 to True
    if ip_addr == '10.220.88.1':
        print("Default gateway IP/Mac is: {}/{}".format(ip_addr, mac_addr))
        found1 = True
    #also finds ip address 10.220.88.30, prints that its found, sets found2 to True
    elif ip_addr == '10.220.88.30':
        print("Arista3 IP/Mac is: {}/{}".format(ip_addr, mac_addr))
        found2 = True

    #breaks loop early if both ip addresses are found: found1 and found2 set to true prints that its exiting
    if found1 and found2:
        print("Exiting...")
        #ends or breaks out of a loop
        break
#blank line
print()