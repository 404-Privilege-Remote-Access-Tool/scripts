import os
import time
from pathlib import Path

statusDir = Path("/tmp/status404")
if(statusDir.is_dir()):
    pass
else:
    os.mkdir("/tmp/status404")

print("sshKeygen automation starting")

customerName = input("Enter the customer name: ")
deviceName = input("Enter the device name: ")
# TO BE FETCHED FROM THE DATABASE
# DEVICE NAME CAN BE DEVICE IP + PORT

keyName = customerName + "-" + deviceName
keyLocation = "/keyDatabase/"

baseDir = Path(keyLocation)
print("keyLocation = " + keyLocation)
if(baseDir.is_dir()):
    print("Directory exists, no need to create the baseDirectory")
else:
    print("Creating baseDirectory")
    os.mkdir(keyLocation)

keyFile = Path(keyLocation + keyName)
keyPath = keyLocation + keyName
print("keyFile = " + keyPath)
if(keyFile.is_file()):
    print("keyFile already exists, skipping the creation operation, please delete the key if you want to update")
    print("WARNING: DELETION OF KEY MAY LEAD TO ADVERSE EFFECTS.")
    os.system("echo '1' > /tmp/status404/keygenStatus")
    exit(1)
else:
    print("File doesn't exists")
    print("Creation of ssh-key started")

returnCode = os.system("ssh-keygen -f " + keyLocation +  keyName + " -t rsa -N ''")
if (returnCode != 0):
    print("ERROR-171, The ssh-key could not be generated")
    os.system("echo '1' > /tmp/status404/keygenStatus")
    exit(1)
else:
    print("sshKey generated sucessfully")
    # SSH-KEY DATABASE TO BE UPDATED IN THE DATABASE
    os.system("echo '0' > /tmp/status404/keygenStatus")
    exit(0)
