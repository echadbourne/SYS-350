# location for vm-utils script

#basic menu
def menu():
    print("[1] VCenter Info")
    print("[2] Session Information")
    print("[3] VM Details")
    print("[0] Exit the program")

def vcenterinfo():
    print("Display vcenter info")

def sessioninfo():
    print("Session Information")

def vmdetails():
    print("VM details")

menu()
print()
option = int(input("Enter yout selection: "))

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
    option = int(input("Enter yout selection: "))

print("Program exiting, goodbye!")