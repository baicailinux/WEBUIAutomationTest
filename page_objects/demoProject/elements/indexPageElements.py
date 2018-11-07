#-*- coding:utf8 -*-
from page_objects.createElement import CreateElement
from page_objects.wait_type import Wait_Type as Wait_By
from selenium.webdriver.common.by import By
class IndexPageElements:
    def __init__(self):
        self.path = '/cloud/project/'
        self.title = CreateElement.create(None,None,None,Wait_By.TITLE_IS,'云主机概况 - 百悟云')
        self.menu_network = CreateElement.create(By.CSS_SELECTOR, '.side_network', '网络',Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.menu_network_secgroup = CreateElement.create(By.LINK_TEXT,'安全组','安全组',Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.user = CreateElement.create(By.CSS_SELECTOR,'li.dropdown:nth-child(2) > a:nth-child(1)',None,Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.user_logout = CreateElement.create(By.CSS_SELECTOR,'#editor_list > li:nth-child(4) > a:nth-child(1)','退出',Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
