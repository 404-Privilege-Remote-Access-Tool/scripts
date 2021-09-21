import os
import time
from pathlib import Path
import getpass

statusDir = Path("/tmp/status404")
if(statusDir.is_dir()):
    pass
else:
    os.mkdir("/tmp/status404")

print("sshCopyId automation starting")

customerName = input("Enter the customer name: ")
deviceName = input("Enter the device name: ")
# TO BE FETCHED FROM THE DATABASE
# DEVICE NAME CAN BE DEVICE IP + PORT

keyName = customerName + "-" + deviceName
keyLocation = "/keyDatabase/"

keyFile = Path(keyLocation + keyName)
keyPath = keyLocation + keyName
print("keyFile = " + keyPath)
if(keyFile.is_file()):
    print("keyFile exists, starting with the sshCopyId process")
else:
    print("File doesn't exists")
    print("Exiting the sshCopyId automation script")
    os.system("echo '1' > /tmp/status404/copyIdStatus")
    exit(1)

adminRemoteUser = "root"
remoteIp = input("Enter the remote system IP: ")
remotePort = input("Enter the remote user port: ")
remotePass = getpass.getpass("Enter the remote user password: ")

copyIdCommand = "yes | PASS=" + '"' + remotePass + '"' + " SSH_ASKPASS=" + '"' + "./ssh-pass.sh" + '"' + " setsid -w ssh-copy-id -i " + keyLocation + keyName + ".pub " + adminRemoteUser + "@" + remoteIp + " -p " + remotePort

# We use setsid -w to disassociate the ssh-copy-id process from the currently used terminal. 
# That forces ssh-copy-id to run the executable specified in the $SSH_ASKPASS in order to obtain the password. 
# We have specified our own script in that variable, so ssh-copy-id will execute just that. 
# Now the script is supposed to provide the password to ssh-copy-id by printing it to its stdout. 
# We use the $PASS variable to the password to the script, so the script just prints that variable.

returnCode = os.system(copyIdCommand)
if (returnCode != 0):
    print("ERROR-172, The ssh-copy-id comand not successful")
    os.system("echo '1' > /tmp/status404/copyIdStatus")
    exit(1)
else:
    print("sshID copied sucessfully")
    # SSH-KEY DATABASE TO BE UPDATED IN THE DATABASE
    os.system("echo '0' > /tmp/status404/copyIdStatus")
    exit(0)
