#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement
from pprint import pprint

'''
Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:

from pprint import pprint
pprint(some_var)


Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
'''
#next three lines allow opening subfolders (using VS code)
from pathlib import Path
data_folder = Path("week2/")
file_to_open = data_folder / "show_arp.txt"

#opens the file show_arp.txt as variable f  
with open(file_to_open) as f:
    sh_arp = f.readlines() #reads each line of show_arp.txt as a list into sh_arp variable

#removed heder from sh arp output the []selects line 1 (which is actuallythe second and no closing means to the end of file)
sh_arp = sh_arp[1:]

#pretty prints the sh_arp variable note this had to be imported (see top of file)
pprint(sh_arp)

#sorts the show_arp list type variable since the actual IP address field are the first unique characters it will sort by IP
sh_arp.sort()

#takes first three arp entries in sorted sh_arp list variable and assignes them to thee_arp
three_arp = sh_arp[:3]

#reassignes the three_arp variable to a string that is joined by the \n character
three_arp = "\n".join(three_arp)

#creates a file arp_entries.txt in write mode with variable f
#need to reassign data_folder, files_to_open, and f this is for VS
#Code subfolder issues. 

data_folder = Path("week2/")
file_to_open = data_folder / "arp_entries.txt"

with open(file_to_open, "w") as f:
    f.write(three_arp) #writes the contents of three_arp variable to f 

