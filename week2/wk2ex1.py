#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement
'''Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. 
Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. 
Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).
'''
#the following three lines are only needed because of VS Code and working directory
from pathlib import Path
data_folder = Path("week2/")
file_to_open = data_folder / "show_version.txt"
#defines variable f to open show_version.txt
f = open(file_to_open)
#defines output veriable to read in contents of show_version.txt
output = f.read()
#prints the output variable (contents of show_version.txt)
print(output)
#prints what type of variable output is (expecting a string here)
print(type(output))
#gracefully closes the show_version.txt file
f.close()

#opens show_version.txt in the more conventional format
with open(file_to_open) as f:
    output2 = f.readlines() #readlines method each line is a list item instead of one big string
#prints the list (since we used readlines()) for output2 variable which is show_version.txt
print(output2)
#prints the variable type of output2(we are expecting a list here)
print(type(output2))