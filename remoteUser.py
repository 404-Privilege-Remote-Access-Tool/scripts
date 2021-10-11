import os
import time
from pathlib import Path

statusDir = Path("/tmp/status404")
if(statusDir.is_dir()):
    pass
else:
    os.mkdir("/tmp/status404")

print("remoteUserCreation automation starting")

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
    os.system("echo '1' > /tmp/status404/remoteUser")
    exit(1)

adminRemoteUser = "root"
remoteIp = input("Enter the remote system IP: ")
remotePort = input("Enter the remote user port: ")

connectionCheckCommand = "ssh -q -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " -p " + remotePort + " exit"
connection = os.system(connectionCheckCommand)
if (connection != 0):
    print("ERROR-121, The ssh connection can not be established")
    os.system("echo '1' > /tmp/status404/remoteUser")
    exit(1)
else:
    print("ssh connection sucessfully established")

issueId = input("Enter the issue id associated: ")
engineerName = input("Enter the engineer name associated: ")
remoteUser = engineerName + "-" + issueId

userCreationCommand = "ssh -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " -p " + remotePort + " useradd " + remoteUser
userCreation = os.system(userCreationCommand)
if (userCreation != 0):
    print("ERROR-173, Remote User can not be created")
    os.system("echo '1' > /tmp/status404/remoteUser")
    exit(1)
else:
    print("remote user succesfully created")
    os.system("echo '0' > /tmp/status404/remoteUser")
    directoryCreationCommand = "ssh -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " mkdir /.scripts"
    os.system(directoryCreationCommand)
    scriptDownloadCommand = "ssh -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " curl https://raw.githubusercontent.com/404-Privilege-Remote-Access-Tool/scripts/master/commandList --output /.scripts/commandList"
    os.system(scriptDownloadCommand)
    scriptDownloadCommand = "ssh -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " curl https://raw.githubusercontent.com/404-Privilege-Remote-Access-Tool/scripts/master/commandValidation.py --output /.scripts/commandValidation.py"
    os.system(scriptDownloadCommand)
    permissionCommand = "ssh -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " chmod +x /.scripts/commandValidation.py"
    os.system(permissionCommand)
    scriptDownloadCommand = "ssh -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " curl https://raw.githubusercontent.com/404-Privilege-Remote-Access-Tool/scripts/master/commandValidator --output /usr/bin/commandValidator"
    os.system(scriptDownloadCommand)
    permissionCommand = "ssh -i " + keyLocation + keyName + " " + adminRemoteUser + "@" + remoteIp + " chmod +x /usr/bin/commandValidator"
    os.system(permissionCommand)
    exit()