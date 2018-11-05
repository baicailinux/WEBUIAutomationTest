#-*- coding:utf8 -*-
from selenium import webdriver

class DriverTool:

    @classmethod
    def get_driver(cls,selenium_hub,browser_type):
        driver=None
        browser_type=browser_type.lower()
        if browser_type=='ie':
            driver = webdriver.Remote(selenium_hub, webdriver.DesiredCapabilities.INTERNETEXPLORER.copy())
        elif browser_type=='firefox':
            driver = webdriver.Remote(selenium_hub, webdriver.DesiredCapabilities.FIREFOX.copy())
        elif browser_type=='chrome':
            driver = webdriver.Remote(selenium_hub, webdriver.DesiredCapabilities.CHROME.copy())
        else:
            return driver
        driver.maximize_window()
        driver.delete_all_cookies()
        return driver