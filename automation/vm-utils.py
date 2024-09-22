# location for vm-utils script
import vconnect
import vsession
import vdetail
#basic menu
def menu():
    print("[1] VCenter Info")
    print("[2] Session Information")
    print("[3] VM Details")
    print("[0] Exit the program")

def vcenterinfo():
    #print("Display vcenter info")
    print()
    print("VCenter Info Selected")
    print()
    vconnect.vconnectfn()

def sessioninfo():
    print()
    print("Session Details Selected")
    print()
    # Contains vcenter username, IP of mgmt box, and the domain name of the vcenter host
    print("~~~~~~~~~~~~~~~~~~~~~~")
    vsession.vsessionfn()
    print("~~~~~~~~~~~~~~~~~~~~~~")

def vmdetails():
    print("VM Details Selected")
    print("~~~~~~~~~~~~~~~~~~~~~~")
    vdetail.vlistfn()
    print("~~~~~~~~~~~~~~~~~~~~~~")
    vm = str(input("Enter the name of your VM. Leave blank if you want all printed: "))
    #match vm name to values, print metadata containing name, state, number of processors, 
    #total memory (might need some math and logic) and ip address (install vmtools on pfsense)

vconnect.vconnectfn()
menu()
print()
option = int(input("Enter your selection: "))

while option != 0:
    if option == 1:
        #Display Vcenter Info
        vcenterinfo()
    elif option == 2:
        #Display Session Information
        sessioninfo()
    elif option == 3:
        #Display VM Details
        vmdetails()
    else:
        print("Please select a valid option")
    print()   
    menu()
    option = int(input("Enter your selection: "))

print("Program exiting, goodbye!")