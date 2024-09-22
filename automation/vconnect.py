#Import the configuration json file and specify the variables

import json
with open('vcenter-conf.json') as i:
    vcenter_conf = json.load(i)


#Specify the information in the json as an array, then use that info to specify variables
vcenter_info = vcenter_conf['vcenter.elizabeth.local'][0]
vhost = vcenter_info['vhost']
vadmin = vcenter_info['vadmin']

import getpass
from pyVim.connect import SmartConnect
import ssl
passw = getpass.getpass()

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode = ssl.CERT_NONE
#Connect to the host with the variables already specified
si = SmartConnect(host=vhost, user=vadmin, pwd=passw, sslContext=s)
content = si.content

def vconnectfn():
    aboutInfo=si.content.about
    print(aboutInfo)
    print(aboutInfo.fullName)

