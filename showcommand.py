#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

@author: kaisar mirza
"""

#from __future__ import absolute_import, division, print_function
#if using python3, then no need for the above line

import json
import netmiko

devices = """
10.10.10.1
10.10.10.2
10.10.10.3
""".strip().splitlines()

device_type = 'cisco_ios'
username = 'admin'
password = 'cisco'

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)

for device in devices:
    try:
        print('~' * 79)
        print('Connecting to device:', device)
        connection = netmiko.ConnectHandler(ip=device, device_type=device_type,
                                            username=username, password=password)
        print(connection.send_command('show ip interface brief'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to ', device, e)
    
