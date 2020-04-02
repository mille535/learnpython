#!/usr/bin/env python
"""
Read in the "show_version.txt" file. From this file use regular expressions to extract the
os_version, serial_number, and configuration register value.
Your output should look as follows:
          OS Version: 15.4(2)T1
       Serial Number: FTX0000038X
     Config Register: 0x2102
"""
from __future__ import unicode_literals, print_function
import re