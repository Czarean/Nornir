#The below code shows you how to manipulate and pull information from specific hosts on our hosts.yml file
#We can filter pretty much anything with python, here you will see a simple way of filtering per:
#-Specific Group
#-Device Name
#-IP address
#-Platform

#CODE:
#Part 1: (Import the required plugins)
from nornir import InitNornir
from nornir.core.filter import F
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

#Part: 2 (Filter the devices that you want using any data that you want)
############ Filter by hostname (IP Address) ############
devices = nr.filter((F(hostname__contains=".4")))

############Filter by group name############
#devices = nr.filter(F(has_parent_group="UK_Showroom_STK"))

############ Filter per Platform ############
#devices = nr.filter((F(platform__contains="cisco_ios")))

############ Filter by device name ############
#devices = nr.filter((F(name__contains=""))) 

#Part 3: (Print the output)
result = devices.run(netmiko_send_command, command_string="sh ver | i uptime")
print_result(result)
