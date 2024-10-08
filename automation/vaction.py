import vconnect
import vdetail
import getpass
import time
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
    for vm in GetVMs:
        if (reqvm == vm.name):
            new_name = input(str("Please enter your new vm name: "))
            print("Renaming from " + vm.name + " to " + new_name)
            vm.Rename(new_name)

def hostcommand(reqvm):
    #Execute a command on a host
    for vm in GetVMs:
        if (reqvm == vm.name):
            user = input("Please enter the username for " + vm.name + " : ")
            print("Please enter the password for " + vm.name)
            password = getpass.getpass()
            creds = vim.vm.guest.NamePasswordAuthentication(username=user, password=password)
            guestosMgr = content.guestOperationsManager
            programPath = "/bin/bash"
            arguments = input(str("Please enter the command you want to execute: "))
            processMgr = guestosMgr.processManager
            processSpec = vim.vm.guest.ProcessManager.ProgramSpec(programPath=programPath, arguments=arguments)
            pid = processMgr.StartProgramInGuest(vm, creds, processSpec)
            while True:
                processInfo = processMgr.ListProcessesInGuest(vm, creds, [pid])[0]
                if processInfo.exitCode is not None:
                    break
                time.sleep(1)
            print("Process exited with code:", processInfo.exitCode)
            #The only way to get the output of the command would be to put it in a file then read that file.
            #I did not have the time to figure this out
            #Check out this link: 
            #https://stackoverflow.com/questions/60318680/how-to-get-a-file-from-a-server-in-a-cluster-in-vsphere-using-pyvmomi-to-remote

#hostcommand("kali2.1")

