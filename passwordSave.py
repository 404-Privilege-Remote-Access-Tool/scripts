import os
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
customerDevicePass = input("Enter the customer password: ")
# TO BE FETCHED FROM THE DATABASE
# DEVICE NAME CAN BE DEVICE IP + PORT

passwordName = customerName + "-" + deviceName
passwordLocation = "/passwordDatabase/"

baseDir = Path(passwordLocation)
print("passwordLocation = " + passwordLocation)
if(baseDir.is_dir()):
    print("Directory exists, no need to create the passwordLocation")
else:
    print("Creating passwordLocation")
    os.mkdir(passwordLocation)

passwordFile = Path(passwordLocation + passwordName)
passwordPath = passwordLocation + passwordName
print("passwordFile = " + passwordPath)
if(passwordFile.is_file()):
    print("passwordFile already exists, skipping the creation operation, please delete the key or perform the update operation if you want to update")
    print("WARNING: DELETION OF KEY MAY LEAD TO ADVERSE EFFECTS.")
    os.system("echo '1' > /tmp/status404/keygenStatus")
    exit(1)
else:
    print("File doesn't exists")
    print("password encryption started")

passwordKeyName = customerName + "-" + deviceName
passwordKeyLocation = "/passwordKeyDatabase/"
passwordKeyDir = Path(passwordKeyLocation)
print("passwordKeyLocation = " + passwordKeyLocation)
if(passwordKeyDir.is_dir()):
    print("Directory exists, no need to create the passwordKeyLocation")
else:
    print("Creating passwordKeyLocation")
    os.mkdir(passwordKeyLocation)

passwordKeyFile = Path(passwordKeyLocation + passwordKeyName)
passwordKeyPath = passwordKeyLocation + passwordKeyName + ".pem"
print("passwordKeyFile = " + passwordKeyPath)
if(passwordKeyFile.is_file()):
    print("passwordKeyFile already exists, skipping the creation operation, please delete the key or perform the update operation if you want to update")
    print("WARNING: DELETION OF KEY MAY LEAD TO ADVERSE EFFECTS.")
    os.system("echo '1' > /tmp/status404/keygenStatus")
    exit(1)
else:
    print("File doesn't exists")
    print("password encryption started")

passwordKey = RSA.generate(2048)
privateKey = passwordKey.exportKey('PEM') 
print(type(privateKey) )
publicKey = passwordKey.publickey()

encryptedDevicePassword = publicKey.encrypt(customerDevicePass.encode('utf-8'),32)

with open(passwordPath, 'wb') as f:
    pickle.dump(encryptedDevicePassword, f)

with open(passwordKeyPath, 'wb') as file:  
    file.write(privateKey)  
