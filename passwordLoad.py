import os
import sys
import time
from pathlib import Path
from Crypto.PublicKey import RSA  
from Crypto.Util import asn1  
from base64 import b64decode  
import pickle

statusDir = Path("/tmp/status404")
if(statusDir.is_dir()):
    pass
else:
    os.mkdir("/tmp/status404")

print("passwordSave functionality starting")

customerName = input("Enter the customer name: ")
deviceName = input("Enter the device name: ")
# TO BE FETCHED FROM THE DATABASE
# DEVICE NAME CAN BE DEVICE IP + PORT

passwordName = customerName + "-" + deviceName
passwordLocation = "/passwordDatabase/"

baseDir = Path(passwordLocation)
print("passwordLocation = " + passwordLocation)
if(baseDir.is_dir()):
    print("Directory exists, continuing with the process")
else:
    print("NO SUCH DIRECTORY EXIT, EXITING THE SCRIPT")
    sys.exit(2)

passwordFile = Path(passwordLocation + passwordName)
passwordPath = passwordLocation + passwordName
print("passwordFile = " + passwordPath)
if(passwordFile.is_file()):
    print("passwordFile exists, continuing with the process")
else:
    print("FILE DOES NOT EXIST, EXITING THE SCRIPT")
    sys.exit(2)

passwordKeyName = customerName + "-" + deviceName
passwordKeyLocation = "/passwordKeyDatabase/"
passwordKeyDir = Path(passwordKeyLocation)
print("passwordKeyLocation = " + passwordKeyLocation)
if(passwordKeyDir.is_dir()):
    print("Directory exists, continuing with the process")
else:
    print("NO SUCH DIRECTORY EXIT, EXITING THE SCRIPT")
    sys.exit(2)

passwordKeyFile = Path(passwordKeyLocation + passwordKeyName + ".pem")
passwordKeyPath = passwordKeyLocation + passwordKeyName + ".pem"
print("passwordKeyFile = " + passwordKeyPath)
if(passwordKeyFile.is_file()):
    print("passwordKeyFile exists, continuing with the process")
else:
    print("FILE DOES NOT EXIST, EXITING THE SCRIPT")
    sys.exit(2)

with open(passwordPath, 'rb') as t:
    encryptedDevicePassword = pickle.load(t)

privateKeyFile = open(passwordKeyPath, 'rb') 
privateKey = RSA.importKey(privateKeyFile.read())

print(privateKey.decrypt(encryptedDevicePassword).decode('utf-8'))

