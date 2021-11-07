#Colby Todd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


"""
To be implemented:
-Crontabs
-AWS
"""

def driver(engine):
    """
    (str) -> none

    Gets browser webdriver and goes to starting page
    """
    if engine == "safari":
        driver = webdriver.Safari()
    elif engine == "chrome":
        driver = webdriver.Chrome()
    elif engine == "firefox":
        driver = webdriver.Firefox()
    elif engine == "edge":
        driver = wedriver.Edge()
    else:
        return 0
    
    driver.get("https://geegeereg.uottawa.ca/geegeereg/Start/start.asp")

def login_information():
    """
    () -> none

    gets login information and then calls site_login
    """
    #opens the file
    file = open("info.txt", "r")

    temp = file.read()

    file.close()

    if  "uname" and "pword" in temp:
        uname = temp.split()[2]
        uname = uname[1:len(uname)-1]

        pword = temp.split()[5]
        pword = pword[1:len(pword)-1]
        
        site_login(uname, pword)

    else:
        uname = input("Enter your username: ").strip()
        pword = input("Enter your password: ").strip()
        
        file = open("info.txt", "w")
    
        temp = repr(uname)
        file.write("uname = " + temp + "\n")

        temp = repr(pword)
        file.write("pword = " + temp + "\n")

        file.close()

        #site_login(uname, pword)

def site_login(uname, pword):
    """
    (str, str) -> none

    logins into the geegee website
    """                                     
    #Navigates to login bar
    #success = False
    #while not(success):
    driver.find_element_by_id("toolbar-login").click()
        #success = check_exists_by_id("ClientBarcode")

    #waits until login page loads
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "ClientBarcode"))) 

    #submits username
    username = driver.find_element_by_id("ClientBarcode")
    username.clear()
    #username.send_keys("")
    username.send_keys(uname)


    #submits password
    password = driver.find_element_by_id("AccountPIN")
    password.clear()
    #password.send_keys("")
    password.send_keys(pword)

    #submits login information
    driver.find_element_by_id("Enter").click()

def book_gym(time):
    """
    (num) -> none
    
    Precondition: time is a number in a 24 hour clock

    books a gym time closes to time
    """
    #Goes to activity page
    driver.get("https://geegeereg.uottawa.ca/geegeereg/Activities/ActivitiesAdvSearch.asp")

    #waits until activity page loads
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[3]/ul/li[3]/span/a")))

    #clicks on fitness and wellness
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[3]/ul/li[3]/span/a").click()

    #waits until fitness and wellness loads
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[7]/td/div[3]/span[1]/a")))

    #clicks on show courses for workout session
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[6]/td/div[3]/span[1]/a").click()

    #waits until workout sessions are shown
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[6]/td/div[3]/div/div/div[2]/div[2]/span/a[2]")))
    
    if time < 16:
        #clicks on page 4
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[7]/td/div[3]/div/div/div[2]/div[2]/span/a[4]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[1]/td[9]/table/tbody/tr[1]/td/span/span/a")))

        if time == 6.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[1]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 7.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[2]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 8:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[3]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 9.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[4]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 10:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[5]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 11.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[6]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 12:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[7]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 13.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[8]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 14:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[9]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 15.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[10]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        else:
            return False
        
    else:
        #clicks on page 5
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[7]/td/div[3]/div/div/div[2]/div[2]/span/a[5]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[1]/td[9]/table/tbody/tr[1]/td/span/span/a")))
        
        if time == 16:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[1]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 17.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[2]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 18:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[3]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 19.5:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[4]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        elif time == 20:
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/table/tbody/tr[3]/td/div[3]/div/div/table/tbody/tr[5]/td[9]/table/tbody/tr[1]/td/span/span/a").click()

        else:
            return False

    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/form/div[3]/div/span/span[1]/input").click()

    driver.find_element_by_xpath(
        "/html/body/div/div[2]/div[1]/form[2]/div/div[6]/span[1]/input").click()

        
#chooses search engine
#driver("safari")
driver = webdriver.Safari()
driver.set_window_size(1000, 1000)
driver.get("https://geegeereg.uottawa.ca/geegeereg/Start/start.asp")

#logins to geegee website
login_information()
#site_login("29003008497811", "133613")

#books the gym time
book_gym(10)
