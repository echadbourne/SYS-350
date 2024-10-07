import vconnect
import vdetail
from pyVmomi import vim

content = vconnect.content
GetVMs = vdetail.GetObjects(content,[vim.VirtualMachine])


def poweron(reqvm):
    for vm in GetVMs:
        if(reqvm == vm.name):
            vm.PowerOn()
            print(vm.name + " Powered on")

#poweron("kali2.1")

def poweroff(reqvm):
    for vm in GetVMs:
        if (reqvm == vm.name):
            vm.PowerOff()
            print(vm.name + " Powered off")

#poweroff("kali2.1")

def reboot(reqvm):
    #soft reboot vm
    for vm in GetVMs:
        if (reqvm == vm.name):
            vm.RebootGuest()
            print(vm.name + " has been sent a request to reboot")

#reboot("kali2.1")


def snapshot(reqvm):
    #snapshot vm
    doublecheck = input(str("This action will power off the selected vm. Do you wish to proceed? [y/n] "))
    if(doublecheck == "y"):
        for vm in GetVMs:
            if (reqvm == vm.name):
                poweroff(reqvm)
                snapshot_name = input(str("Please insert the name of the snapshot: "))
                description = input(str("Please type a description for the snapshot: "))
                vm.CreateSnapshot(snapshot_name, description, False, False)
                print("Snapshot created for " + vm.name)
                #values dump_memory and quiesce are automatically set to false
    else:
        print ("action cancelled, aborting")

#snapshot("kali2.1")

def rename(reqvm):
    #rename a vm
    for vm in GetVms:
        if (reqvm == vm.name):
            new_name = input(str("Please enter your new vm name: "))
            print("Renaming from " + vm.name + " to " + new_name)
            vm.Rename(new_name)

def hostcommand(reqvm):
    #Execute a command on a host
    print("Can only be used on Linux based vms at this time")
    for vm in GetVMs:
        if (reqvm == vm.name):
            guestosMgr = vm.guestOperationsManager
            programPath = "/bin/bash"
            arguments = input(str("Please enter the command you want to execute: "))
            processMgr = guestosMgr.processManager
            processSpec = vim.vm.guest.ProcessManager.ProgramSpec(programPath=programPath, arguments=arguments)
            pid = processMgr.StartProgramInGuest(vm, processSpec)
            while True:
                processInfo = processMgr.ListProcessesInGuest(vm, [pid])[0]
                if processInfo.exitCode is not None:
                    break
                time.sleep(1)
            print("Process exited with code:", processInfo.exitCode)

hostcommand("kali2.1")

