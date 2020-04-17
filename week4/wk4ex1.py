#!/usr/bin/env python
"""
Create a dictionary representing a network device. The dictionary should have key-value pairs
representing the 'ip_addr', 'vendor', 'username', and 'password' fields.
Print out the 'ip_addr' key from the dictionary.
If the 'vendor' field is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' field is
'juniper', then set the 'platform' to 'junos'.
Create a second dictionary named bgp_fields. The bgp_fields should have a key for 'bgp_as',
'peer_as', and 'peer_ip'.
Using the .update() method add the bgp_fields key-value pairs to the network device dictionary.
Using a for-loop iterate over the dictionary and print out all of the dictionary keys.
Using a single for-loop iterate over the dictionary and print out all of the dictionary keys and
values.
"""

from __future__ import unicode_literals, print_function

router1 = {
    "ip_addr": "172.16.1.1",
    "vendor": "Cisco",
    "username": "admin",
    "password": "monkey123"
}

print()
print(router1['ip_addr'])
print()

if router1['vendor'].lower() == 'cisco':
    router1['platform'] = 'ios'
elif router1['vendor'].lower() == 'juniper':
    router1['platform'] = 'junos'

bgp_fields = {
    "bgp_as": "1254",
    "peer_as": "5423",
    "peer_ip": "172.16.1.2"
}

router1.update(bgp_fields)

print('-' * 80)
for i in router1:
    print("{:>15}".format(i))

print('-' * 80)
print()

print('-' * 80)
for key, value in router1.items():
    print("{key:>15} ---> {value:>15}".format(key=key, value=value))

print('-' * 80)
print()
