#!/usr/bin/python3

import requests
import time
from UserAccount import *
from TimeClockBot import *
from requests.exceptions import RequestException
from selenium import webdriver

def autorunbot(botinstance, useraccount):
    botinstance.logintoamazon(useraccount.useralias, useraccount.userpin)
    botinstance.grabcompanytime()
    botinstance.grabcompanydate()
    botinstance.punchout()
    botinstance.clickcontinue()
    botinstance.inputstarttime()
    botinstance.clickcontinue()
    botinstance.clickcontinue()
    botinstance.clickyes()
    # Finishes Clocking in
    # bot.clickcontinue()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Chris = UserAccount()
    Chris.grabaccountdata()
    bot = TimeClockBot()
    autorunbot(bot, Chris)


