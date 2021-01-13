from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import keys

class Bot:
    
    def __init__(self, browser):
        self.webdriver=browser

    def login(self, username, password):
        sleep(2)
        webdriver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        sleep(3)
        username1= webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input')
        username1.send_keys(username)  #specify username
        password1 = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input')
        password1.send_keys(password)  #specify password
        sleep(5)
        try:
            button_login = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button')
        except:
            button_login = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[4]/button')
        button_login.click()
        webdriver.get('https://www.linkedin.com/mynetwork/')
        sleep(3)
        dropdown = webdriver.find_element_by_xpath('/html/body/div[8]/aside/div[1]/header/section[2]/button[2]')
        dropdown.click()
        sleep(3)
        seeall = webdriver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div/div/ul/li[1]/div/button/span')
        seeall.click() 
        sleep(4)


    # =============================================================================
    # Rapidly send connection requests
    # =============================================================================
    def rapidfollow(self):
        for i in range(1,1000):
            sleep(2)
            one="/html/body/div[4]/div/div/div[2]/ul/li["                  
            two="]/div/section/div[2]/footer/button/span"
            total=one+str(i)+two
            connect = webdriver.find_element_by_xpath(total)
            connect.click() 
            if i%12==0:
                sleep(3)

webdriver = webdriver.Chrome(executable_path=keys.cd_path)
a=Bot(webdriver)
a.login(keys.username, keys.password)
a.rapidfollow()
