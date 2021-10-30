#!/usr/bin/env python
# coding: utf-8

# In[70]:

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os

def checkin(username, password):
#     try:
        
    daka = "https://www.ablesci.com/site/login"
    driver = webdriver.Chrome()
    driver.get(daka)
    
    sleep(3)
    driver.find_element_by_id("LAY-user-login-email").send_keys("{}".format(username))
    driver.find_element_by_id("LAY-user-login-password").send_keys("{}".format(password))
    driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div[1]/div/div/div/div/div/div[4]/button").click()

    sleep(3)

    element=driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/button")
    element.click()

    #关闭浏览器
    sleep(3)
    driver.quit()
    print("success")
#     except Exception as e:
#         print("fail")
#         pass

checkin(username = os.environ["USERNAME"],
        password = os.environ["PASSWORD"])


# In[ ]:




