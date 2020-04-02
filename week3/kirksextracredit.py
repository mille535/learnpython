'''
Kirk Miller 2020
My First LAN Scanner: A very rudimentary IP address scanner. There are many, many, many ways
this could be proved but is something I wanted to try to do while learning Python. I may add
more features and improve the code as I learn. Some things I'd like to possibly add:

* User and/or command line input of subnet
* OS detection
* A nicer way of outputting to the screen, maybe showing more than just whats up but IP arr
    and status
* Add option to write output to the screen or a text file

'''
from __future__ import unicode_literals, print_function
import os
from pprint import pprint

WINDOWS = True

base_ip = '172.17.1.'
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'

base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_list = []

for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)

alive_ips = []
#test case, lowering the amount of ips in ip_list so it doesnt take 15 minutes to run
#ip_list = ip_list[2:6]

for i in ip_list:
    result = os.popen("{} {}".format(base_cmd, i)).read()
    if "unreachable" in result.lower():
        continue
    elif "bytes=32" in result.lower():
        alive_ips.append(i)

pprint(alive_ips)