#!/usr/bin/python3
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TimeClockBot:
    def __init__(self):
        self.endtime = ""
        self.companydate = ""
        # Path of the executable of chromedriver.exe
        # TODO Implement walking the directory tree and searching for file directly
        driverpath = "D:\Downloads\chromedriver.exe"
        options = webdriver.ChromeOptions()
        # selenium normally uses a temp browser profile,
        # in order to use our own account we specify our own user data
        # r before string start is to create a raw string, alt fix is double all the backslashes
        options.add_argument(
            r"user-data-dir=C:\Users\Cuhwis\AppData\Local\Google\Chrome\User Data\Selenium Profile")  # Path to user data
        # Once bot is init creates webdriver specific to Chrome
        # executable_path is chrome driver path location, chrome_options is userdata path
        self.driver = webdriver.Chrome(executable_path=driverpath, options=options)

    def logintoamazon(self, alias, pin):
        try:
            self.driver.get("https://281685.tcplusondemand.com/app/webclock/#/EmployeeLogOn/281685")
            # Wait for site to load find input form for "badgeNumber"
            badgenumberelement = WebDriverWait(self.driver, 6).until(
                EC.presence_of_element_located((By.ID, "LogOnEmployeeId")))
            badgenumberelement.send_keys(alias)
            time.sleep(2)
            logonelement = self.driver.find_element_by_xpath("//*[@value='Log On To Dashboard']")
            logonelement.click()
            # Reassign value of endtime, need for later
            time.sleep(2)
            pinelement = WebDriverWait(self.driver, 6).until(
                EC.presence_of_element_located((By.ID, "LogOnEmployeePin")))
            time.sleep(1)
            pinelement.send_keys(pin)
            logonelement2 = self.driver.find_element_by_xpath("//*[@value='Log On']")
            logonelement2.click()
            time.sleep(2)
            if self.driver.title == "My Dashboard":
                # Log success
                print(f"Successfully Logged In at {datetime.now()}")
            else:
                # Failed attempt
                print(f"Failed Logging In at {datetime.now()}")

        except Exception as e:
            print("Something went wrong " + str(e))

    def grabcompanytime(self):
        companytime = self.driver.find_element_by_xpath("//*[@class='CompanyTime']")
        self.endtime = companytime.text
        print(companytime.text)
        return companytime.text

    def grabcompanydate(self):
        companydate = self.driver.find_element_by_xpath("//*[@class='CompanyDate']")
        self.companydate = companydate.text
        return companydate.text

    def punchout(self):
        punchoutelement = WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//*[@value='Punch Out']")))
        punchoutelement.click()

    def clickcontinue(self):
        continueelement = WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//*[@value='Continue']")))
        continueelement.click()

    def clickyes(self):
        yeselement = WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located((By.XPATH, "//*[@value='Yes']")))
        yeselement.click()

    # TODO should be taking input of starttime
    def inputstarttime(self, workdaylength=8, lunchlength=30):
        # TODO account for if workday length > time & time is AM then minus 1 day from workday
        # 08:01:58 PM
        time.sleep(1)
        # Format of time strings
        # %I (12-hour clock) as a zero-padded decimal number.
        formatoftime = "%I:%M:%S %p"
        # Get starttime 8 1/2 hours before time now (30 min for lunch)
        timetostart = datetime.strptime(self.endtime, formatoftime) - timedelta(hours=workdaylength,
                                                                                minutes=lunchlength)
        # Log message
        print(
            f"Converted {self.endtime} - {workdaylength} hours, {lunchlength} minutes to {str(timetostart)} at {datetime.now()}")
        inputtimeelement = self.driver.find_element_by_xpath(
            "//*[@id='featureForm']/div[2]/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/input[2]")
        inputtimeelement.clear()
        # Get hours and minute from datetime object as string
        starttime = timetostart.time()
        inputtimeelement.send_keys(str(starttime))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot = TimeClockBot()
    bot.logintoamazon("test", "0000")
    bot.endtime = bot.grabcompanytime()
    bot.punchout()
    bot.clickcontinue()
    bot.inputstarttime()
    bot.clickcontinue()
