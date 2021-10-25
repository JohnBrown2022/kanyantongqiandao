#!/usr/bin/env python
# coding: utf-8

# In[70]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def checkin(username, password):
    try:
        #登录
        daka = "https://www.ablesci.com/site/login"
        driver = webdriver.Chrome()
        driver.get(daka)
        driver.find_element_by_id("username").send_keys("{}").format(username)
        driver.find_element_by_id("password").send_keys("{}").format(password)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/form/div/div[1]/div/div/div/div/div/div[4]/button").click()

        sleep(3)

        element=driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/button")
        element.click()

        #关闭浏览器
        sleep(3)
        driver.quit()
    except Exception as e:
    pass

checkin("1846128548@qq.com", "calman.qzy.")


# In[ ]:




