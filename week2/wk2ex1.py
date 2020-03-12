#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement
'''Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file contents to a variable. 
Print out the file contents to the screen. Also print out the type of the variable (you should have a string at this point).

Close the file.

Open the file a second time using a Python context manager (with statement). Read in the file contents using the .readlines() method. 
Print out the file contents to the screen. Also print out the type of the variable (you should have a list at this point).
'''

#defines variable f to open show_version.txt
f = open("show_version.txt")
#defines output veriable to read in contents of show_version.txt
output = f.read()
#prints the output variable (contents of show_version.txt)
print(output)
#prints what type of variable output is (expecting a string here)
print(type(output))
#gracefully closes the show_version.txt file
f.close()

#opens show_version.txt in the more conventional format
with open("show_version.txt") as f2:
    output2 = f2.readlines() #readlines method each line is a list item instead of one big string
#prints the list (since we used readlines()) for output2 variable which is show_version.txt
print(output2)
#prints the variable type of output2(we are expecting a list here)
print(type(output2))