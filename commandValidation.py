import os
import sys
import time
from pathlib import Path

command = input("Enter the command: ")

while command != 'sshExit':
    commandFile = open("/.scripts/commandList", "r")
    commandAvailable = commandFile.read()
    commandAvailableList = commandAvailable.split("\n")

    if command.split(' ', 1)[0] in commandAvailableList:
        os.system(command)
    else:
        print("Comand permission not granted, please connect with the admin")

    command = input("Enter the command: ")

