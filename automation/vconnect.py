#vconnect script

import getpass
from pyVim.connect import SmartConnect
import ssl
passw = getpass.getpass()


def vconnectfunction():
    s=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    s.verify_mode=ssl.CERT_NONE
    si= SmartConnect(host="vcenter.elizabeth.local", user="elizabeth-adm@elizabeth.local", pwd=passw, sslContext=s)
    aboutInfo=si.content.about
    print(aboutInfo)
    print(aboutInfo.fullName)

vconnectfunction()