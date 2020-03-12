#!/usr/bin/env python
from __future__ import print_function, unicode_literals, with_statement
'''
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to 
the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''
#creates a list of 5 IP addresses
ip_list = ["24.220.208.82", "4.2.2.2", "8.8.8.8", "24.220.0.10", "192.168.45.2"]

#adds single IP to the end of the list using append() method
ip_list.append("172.24.21.17")

#add two additional IPs to the end of the list using .extend() method
ip_list.extend(["10.11.12.13", "10.47.21.14"])

#adds yet another two IP addresses to the list by concantonating the ip_list
ip_list = ip_list + ['172.16.1.1', '172.16.1.2']

#prints the entire list
print(ip_list)

#prints the first address in list
print(ip_list[0])

#prints last address in the list
print(ip_list[-1])

#removed the first item from the list
ip_list.pop(0)

#removes the last item from the list
ip_list.pop()

#changes the first item in the list to 2.2.2.2
ip_list[0] = "2.2.2.2"

#prints the first item in the list
print(ip_list[0])