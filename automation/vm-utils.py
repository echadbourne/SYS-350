# location for vm-utils script
import vconnect
import vsession
import vdetail
import vaction


#basic menu
def menu():
    print("[1] VCenter Info")
    print("[2] Session Information")
    print("[3] VM Details")
    print("[4] VM Actions")
    print("[0] Exit the program")

def actions():
    print("[1] Power On VM")
    print("[2] Power Off VM")
    print("[3] Reboot VM")
    print("[4] Snapshot VM")
    print("[5] Rename VM")
    print("[6] Execute Command on VM")

vconnect.vconnectfn()
menu()
print()
option = int(input("Enter your selection: "))

while option != 0:
    if option == 1:
        print()
        print("VCenter Info Selected")
        print()
        vconnect.vconnectfn()
    elif option == 2:
        print()
        print("Session Details Selected")
        print()
        # Contains vcenter username, IP of mgmt box, and the domain name of the vcenter host
        print("~~~~~~~~~~~~~~~~~~~~~~")
        vsession.vsessionfn()
        print("~~~~~~~~~~~~~~~~~~~~~~")
    elif option == 3:
        print("VM Details Selected")
        vdetail.vdetails(vdetail.GetVMs)
    elif option == 4:
        vdetail.vlist(vdetail.GetVMs)
        vmselect = str(input("Please select a vm: ")) #This goes in the functions as a parameter
        actions()
        vmaction = int(input("Please select an action, 0 for none: ")) #This is used for the menu to select the right action function
        print("test1")
        #use functions from other files, they should have a
        #"vm" parameter so just insert vmselect there
        print(vmaction)
        #bunch of else and elif running the proper functions
        while vmaction != 0:
            if vmaction == 1:
                #power on vm
                vaction.poweron(vmselect)
                break
            elif vmaction == 2:
                #power off vm
                print(vmaction)
                print("Power off selected")
                vaction.poweroff(vmselect)
                break
            elif vmaction == 3:
                #soft reboot vm
                vaction.reboot(vmselect)
                break
            elif vmaction == 4:
                #snapshot vm
                vaction.snapshot(vmselect)
                break
            elif vmaction == 5:
                vaction.rename(vmselect)
                #rename vm
                break
            elif vmaction == 6:
                #execute command on vm
                print("Can only be used on Linux based vms at this time")
                vaction.hostcommand(vmselect)
                break

        else:
            print("Please select a valid action")
            print()
            actions()
            vmaction = str(input("Please select an action, 0 for none: "))

    else:
        print("Please select a valid option")
        print()   
        menu()
        option = int(input("Enter your selection: "))

print("Program exiting, goodbye!")