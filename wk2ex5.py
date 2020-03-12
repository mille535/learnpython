#!/usr/bin/env python
from __future__ import print_function, unicode_literals
"""Read the 'show_ip_bgp_summ.txt' file into your program. From this
BGP output obtain the first and last lines of the output.
From the first line use the string .split() method to obtain the local
AS number. From the last line use the string .split() method to
obtain the BGP peer IP address. Print both local AS number and the
BGP peer IP address to the screen.
"""
#opens file and reads lines into list type variable
with open("show_ip_bgp_summ.txt") as f:
    bgp_lines = f.readlines()

#set asn variable to first line and last field of bgp_lines variable
asn = bgp_lines[0].split()[-1]

"""
set peer_ip variable to last line and first field of bgp_lines 
it should be noted that to get to the fields level I am using
the .split() function
"""

peer_ip = bgp_lines[-1].split()[0]
print("Local BGP AS: {} Peer IP: {}".format(asn, peer_ip))
