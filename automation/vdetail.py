#contains the vdetail function
import vconnect
from pyVmomi import vim #not imported with vconnect

content = vconnect.content

def GetObjects(content, ObjType):
    obj = {}
    Holding = content.viewManager.CreateContainerView(content.rootFolder, ObjType, True)
    for MObject in Holding.view:
        obj.update({MObject:MObject.name})
    return obj

def vlistfn():
    VMList = GetObjects(content,[vim.VirtualMachine])
    for vm in VMList:
        print (vm.name)

def vdetailfn()
    
