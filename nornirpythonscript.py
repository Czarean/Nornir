#This is the Python code that we execute to run whatever we want to accomplish
#In this example we retrieve the host uptime information from all our nodes that are on the host.yml file

from nornir import InitNornir                                               # This code imports and begin Nornir functions on the code
from nornir_netmiko.tasks import netmiko_send_command                       # Imports the netmiko task needed to send show commands to the hosts "netmiko_send_command"
from nornir_utils.plugins.functions import print_result                     # Imports the Nornir function needed to print code into the terminal

nr = InitNornir(config_file="config.yml")                                   # This code initiates nornir and tells python where to look for the passwords needed to SSH, our network devices and groups to which network devices belongs to.
                                                                            # by default it will run the tasks on all the hosts inside the hosts.yml file unless we specifically filter the hosts.yml file 
                                                                                  
result = nr.run(netmiko_send_command, command_string="sh ver | i uptime")   # Here we create the variable named "result", which will send whatever command we tell it to send
print_result(result)                                                        # Prints the result variable



#######################################################################################################################################

# To run the python script go to your terminal, go to the path where you have the python script saved 
# Once there just run it with the following command: python3 nornirpythonscript.py
# Example: cesaranaya@MacBook-Pro-8 NornirTest % python3 nornirpythonscript.py
