#!/usr/bin/env python
from netmiko import ConnectHandler

cisco_iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.122.254',
    'username': 'kaisar',
    'password': 'cisco',
#   'port' : 8022,          # optional, defaults to 22
#   'secret': 'secret',     # optional, defaults to ''
#   'verbose': False,       # optional, defaults to False
}
net_connect = ConnectHandler(**cisco_iosv_l2)
output = net_connect.send_command('show ip int brief')
print(output)


config_commands = [ 'int loop 20',
                    'ip address 20.20.20.20 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)


for n in range (120,131):
                print "Creating VLAN" + str(n)
                config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n) ]
                output = net_connect.send_config_set(config_commands)
                print output
