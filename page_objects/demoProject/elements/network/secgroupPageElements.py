#-*- coding:utf-8 -*-
from page_objects.createElement import CreateElement
from page_objects.wait_type import Wait_Type as Wait_By
from selenium.webdriver.common.by import By
class SecgroupPageElements:
    def __init__(self):
        self.title=CreateElement.create(None,None,None,Wait_By.TITLE_IS,'安全组 - 百悟云')
        self.search=CreateElement.create(By.NAME,'security_groups__filter__q','筛选',Wait_By.PRESENCE_OF_ELEMENT_LOCATED)