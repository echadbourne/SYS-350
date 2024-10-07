#contains the vdetail function
import vconnect
from pyVmomi import vim #not imported with vconnect


content = vconnect.content

#Big thanks to natalie for help with the vlistfn

def GetObjects(content, ObjType):
    obj = {}
    Container = content.viewManager.CreateContainerView(content.rootFolder, ObjType, True)
    for MObject in Container.view:
        obj.update({MObject:MObject.name})
    return obj

GetVMs = GetObjects(content,[vim.VirtualMachine])

def vdetails(VMList):
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("VM Names:")
    for vm in VMList:
        print(vm.name)
    print("~~~~~~~~~~~~~~~~~~~~~~")
    reqvm = str(input("Enter vm (leave blank if none): "))


    if(reqvm):
        for vm in VMList:
            if(vm.name == reqvm):
                print("~~~~~~~~~~~~~~~~~~~~~~")
                print ("Name: " + vm.name)
                print (f"IP Address: {vm.guest.ipAddress}")
                print ("Power State: " + vm.runtime.powerState)
                print (f"CPU: {vm.config.hardware.numCPU}")
                Memory = int(vm.config.hardware.memoryMB) / 1024
                print (f"Memory (GB): {Memory}")
                print("~~~~~~~~~~~~~~~~~~~~~~")

    else:
        for vm in VMList:
            print("~~~~~~~~~~~~~~~~~~~~~~")
            print ("Name: " + vm.name)
            print (f"IP Address: {vm.guest.ipAddress}")
            print ("Power State: " + vm.runtime.powerState)
            print (f"CPU: {vm.config.hardware.numCPU}")
            Memory = int(vm.config.hardware.memoryMB) / 1024
            print (f"Memory (GB): {Memory}")
            print("~~~~~~~~~~~~~~~~~~~~~~")
    

def vlist(VMList):
    VMList = GetObjects(content,[vim.VirtualMachine])
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("VM Names and Power State:")
    for vm in VMList:
        print(vm.name + vm.runtime.powerState)
    print("~~~~~~~~~~~~~~~~~~~~~~")

