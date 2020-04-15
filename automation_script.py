# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 04:17:20 2020

@author: Parth
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'C:/Users/Parth/Contacts/Downloads/chromedriver_win32/chromedriver.exe'
#chromedriver_path = 'C:\Users\Parth\Contacts\Downloads\chromedriver_win32\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
sleep(3)

# =============================================================================
# Login
# =============================================================================
username = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input')
username.send_keys('')  #specify username
password = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input')
password.send_keys('')  #specify password
sleep(5)
try:
    button_login = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[3]/button')
except:
    button_login = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[4]/button')
button_login.click()
sleep(3)

# =============================================================================
# Navigate to your connections
# =============================================================================
notnow = webdriver.find_element_by_xpath('/html/body/header/div/nav/ul/li[2]/a/span[1]')
notnow.click() 
sleep(4)
seeall = webdriver.find_element_by_xpath('/html/body/div[5]/div[3]/div[3]/div/div/div/div/div/div/ul/li[1]/div/button/span')
seeall.click() 
sleep(4)


# =============================================================================
# Rapidly send connection requests
# =============================================================================
for i in range(1,1000):
    sleep(2)
    one="/html/body/div[4]/div/div/div[2]/ul/li["
    two="]/div/section/div[2]/footer/button/span"
    total=one+str(i)+two
    connect = webdriver.find_element_by_xpath(total)
    connect.click() 
    if i%12==0:
        sleep(3)
    




