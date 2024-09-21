#Contains code for the session information function

import socket
import getpass

def vsessionfn()
    #Save hostname to variable with socket
    hostname = socket.gethostname()
    #Get IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.0.0.0', 0))
    #Save IP address to variable
    IPAddress = s.getsockname()[0]
    #print hostname and IP address
    print("Hostname: " + hostname)
    print("IP Address: " + IPAddress)
    #Use getpass to save current user to variable
    current_user = getpass.getuser()
    #print current logged in user
    print("Current Logged in User: " + current_user) #prints user logged into mgmt box

#Figure out how to get vcenter logged in user?


