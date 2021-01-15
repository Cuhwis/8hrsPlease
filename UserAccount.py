#!/usr/bin/python3

import json
import os
import getpass
from datetime import datetime
from pathlib import Path


class UserAccount:

    def __init__(self):
        self.useralias = ""
        self.userpin = ""
        self.startshift = ""
        self.startlunch = ""
        self.endlunch = ""
        # TODO let user choose name askfilename()
        self.filename = r"\accountdata.json"
        # Get users profile name
        self.currentuser = getpass.getuser()
        self.filedirectory = fr"\Users\{self.currentuser}\Documents"
        self.filepath = Path(self.filedirectory + self.filename)

    def grabaccountdata(self):
        try:
            if Path.exists(self.filepath):
                self.readaccountdata()
            else:
                print(f"{self.filename} doesn't exist in {self.filedirectory}")
                self.createaccountdata()
        except Exception as e:
            print("Something went wrong " + str(e))
    def createaccountdata(self):
        # Data structure
        data = {
            "user": {
                "alias": "",
                "pin": "",
                "startshift": "",
                "endshift": "",
                "startlunch": "",
                "endlunch": "",
            }
        }
        # Write to accountdata.txt having user set the values
        with open(self.filepath, "w") as accountdata:
            # Success message
            print(f"Created {self.filename}")
            # Populate Data
            while True:
                for x in data["user"].keys():
                    valueofkey = data["user"][x]
                    if valueofkey == "":
                        #no echoing when entering pin
                        if x == "pin":
                            # TODO Implement echo off for secure pin entry
                            pin = input(f"Please set value for {x}: ")
                            data["user"][x] = pin
                        else:
                            data["user"][x] = input(f"Please set value for {x}: ")
                isdatagood = input(f"Is this data good? Won't be able to change later [Y/N]: \n")
                if isdatagood.lower() == "y":
                    break
                else:
                    print("Chose to reenter data / Invalid input reentering data anyway")
                    for x in data["user"].keys():
                        #TODO Find a way to implement it on not just screens
                        data["user"][x] = ""

            # Write data to file
            json.dump(data, accountdata)
            print(f"Account data populated at {datetime.now()}")

    def readaccountdata(self):
        # Read the date from accountdata.json
        with open(self.filepath, "r") as accountdata:
            accountdata = json.load(accountdata)
            self.useralias = accountdata["user"]["alias"]
            self.userpin = accountdata["user"]["pin"]
            self.startshift = accountdata["user"]["startshift"]
            self.startlunch = accountdata["user"]["startlunch"]
            self.endlunch = accountdata["user"]["endlunch"]


if __name__ == '__main__':
    Chris = UserAccount()
    Chris.grabaccountdata()