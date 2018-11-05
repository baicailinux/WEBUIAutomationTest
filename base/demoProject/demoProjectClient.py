# -*- coding:utf-8 -*-
from base.demoProject.demoProjectReadConfig import DemoProjectReadConfig
from base.readConfig import ReadConfig
from common.selenium.browserOperator import BrowserOperator
from common.selenium.driverTool import DriverTool
from page_objects.demoProject.pages.loginPage import LoginPage
class DemoProjectClient:
    def __init__(self,browserOperator_type=0):
        """
        :param browserOperator_type:0-未登录、1-已登录
        """
        self.config=ReadConfig().config
        self.demoProjectConfig=DemoProjectReadConfig().config

        self.driver = DriverTool.get_driver(self.config.selenium_hub, self.demoProjectConfig.browser_type)
        self.driver.get(self.demoProjectConfig.web_host + '/cloud/auth/login/')
        self.browserOperator = BrowserOperator(self.driver)
        if browserOperator_type==1:
            loginPage=LoginPage(self.browserOperator)
            loginPage.loginSuccess(self.demoProjectConfig.normal_username, self.demoProjectConfig.normal_password)