import os
import pickle
from get_credentials import get_creds
from time import sleep
from selenium import webdriver

if os.path.exists('credentials.pickle'):
    with open('credentials.pickle','rb') as f:  
        credentials = pickle.load(f)
else:
    get_creds()
    with open('credentials.pickle','rb') as f:  
    	credentials = pickle.load(f)

EXECUTABLE_PATH = credentials['EXECUTABLE_PATH']
LINKEDIN_PATH = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
BROWSER = credentials['Browser']
EMAIL_OR_PHONE_NO = credentials['Email_or_phone_no']
PASSWORD = credentials['Password']

print(credentials)

if BROWSER == "Chrome":
    webdriver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
elif BROWSER == "Firefox":
    webdriver = webdriver.Firefox(executable_path=EXECUTABLE_PATH)

webdriver.get(LINKEDIN_PATH)
sleep(3)

# =============================================================================
# Login
# =============================================================================
email_or_phone_no = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[1]/input')
email_or_phone_no.send_keys(EMAIL_OR_PHONE_NO) 
password = webdriver.find_element_by_xpath('/html/body/div/main/div[2]/form/div[2]/input')
password.send_keys(PASSWORD)  
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
    connect.click("/html/body/div[4]/div/div/div[2]/ul/li[{i}]/div/section/div[2]/footer/button/span") 
    if i%12==0:
        sleep(3)