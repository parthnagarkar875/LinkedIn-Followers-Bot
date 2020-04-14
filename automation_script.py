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

chromedriver_path = '/usr/bin/chromedriver' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('')  #specify username
password = webdriver.find_element_by_name('password')
password.send_keys('')  #specify password
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div > button')
button_login.click()
sleep(3)
notnow = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN> div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications


hashtag_list = ['fcbarcelona', 'chelsea', 'manchestercity']

prev_user_list = [] #- if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,
#                  1:2]  # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    first_thumbnail.click()
    sleep(randint(1, 2))
    try:
        for x in range(1, 200):
            username = webdriver.find_element_by_xpath(
                '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text

            if username not in prev_user_list:
                # If we already follow, do not unfollow
                if webdriver.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                    webdriver.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath(
                        '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

                    button_like.click()
                    likes += 1
                    sleep(randint(18, 25))
                    comments += 1
                    webdriver.find_element_by_xpath(
                            '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                    comment_box = webdriver.find_element_by_xpath(
                            '/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                    comment_box.send_keys('Really cool!')
                    sleep(3)

                # Enter to post comment
                    comment_box.send_keys(Keys.ENTER)
                    sleep(randint(22, 28))
                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(25, 29))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(20, 26))
                # sleep(2)
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0, len(new_followed)):
    prev_user_list.append(new_followed[n])

updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
