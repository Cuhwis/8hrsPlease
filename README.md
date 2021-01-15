
# Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Resources Utilized](#resources-utilized)
- [How To Use](#how-to-use)


## Introduction
![MrGates](https://i.pinimg.com/originals/dc/ff/68/dcff6879a71fcfb100a7de1cf18f5803.jpg)
# 8hrsPlease - Amazon SDE Appenticeship Project
Python development utilizing cirriculum learned over the past 2 weeks. 8hrsPlease is an application developed to minimize trouble tickets associated with my account.

## Requirements

 - User Accessibility 
  1. User shall be able to create own account data
  2. User shall be able to utilize newly created json file to run bot
  3. User shall be able to specify parameters and customizations to run bot a certain way
  4. User shall be able to run program at anytime of day
  
 - System Accessibility 
  1. System shall take input from user and create JSON file with data
  2. System shall read from accountdata.json and assign data to UserAccount instance
  2. System shall utilize selenium in order populate webdriver
  3. System shall perform functions on webdriver on certain elements of web page
  4. System shall take attributes from instance of UserAccount.py and pass to functions defined in TimeClockBot.py
 - Software 
  1. System shall be written in Python, using IDE (PyCharm)

## Resources Utilized

 - Python 3
 - PyCharm
 - Selenium
 - OS
 - DateTime
 - pathlib

## How To Use
 1. **Find Chrome Version Number**
![WireFrame](https://i.imgur.com/isKnupy.jpg)

 2. **Download ChromeDriver** [Driver download](https://chromedriver.chromium.org/downloads)
 3. **Place .exe in filepath** I use the file path "D:\Downloads\chromedriver.exe" If you use a different file path change driverpath value in TimeClockBot.py
 4. **Start the program** run main.py!
