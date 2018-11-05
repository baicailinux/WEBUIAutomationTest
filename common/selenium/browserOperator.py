#-*- coding:utf8 -*-
from common.dateTimeTool import DateTimeTool
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from page_objects.wait_type import Wait_Type  as Wait_By
import allure
class BrowserOperator:
    def __init__(self,driver):
        self._driver=driver

    def get(self,url):
        self._driver.get(url)

    def get_current_url(self):
        return self._driver.current_url.encode('utf-8')

    def getTitle(self):
        return self._driver.title.encode('utf-8')

    def getText(self,elementInfo):
        webElement=self.getElement(elementInfo)
        return webElement.text.encode('utf-8')

    def click(self,elementInfo):
        webElement=self.getElement(elementInfo)
        webElement.click()

    def sendText(self,elementInfo,text):
        text=text.decode('utf-8')
        webElement=self.getElement(elementInfo)
        webElement.clear()
        webElement.send_keys(text)

    def is_displayed(self,elementInfo):
        webElement=self.getElement(elementInfo)
        flag=webElement.is_displayed()
        return flag

    def is_enabled(self,elementInfo):
        webElement = self.getElement(elementInfo)
        flag = webElement.is_enabled()
        return flag

    def is_selected(self,elementInfo):
        webElement = self.getElement(elementInfo)
        flag = webElement.is_selected()
        return flag

    def select_dropDownBox_by_value(self,elementInfo,value):
        """
        适用单选下拉框
        :param elementInfo:
        :param value:
        :return:
        """
        webElement= Select(self.getElement(elementInfo))
        webElement.select_by_value(value)

    def select_dropDownBox_by_text(self,elementInfo,text):
        """
        适用单选下拉框
        :param elementInfo:
        :param text:
        :return:
        """
        webElement= Select(self.getElement(elementInfo))
        webElement.select_by_visible_text(text)

    def select_dropDownBox_by_index(self,elementInfo,index):
        """
        适用单选下拉框,下标从0开始
        :param elementInfo:
        :param index:
        :return:
        """
        webElement= Select(self.getElement(elementInfo))
        webElement.select_by_index(index)

    def select_dropDownBox_by_values(self,elementInfo,values):
        """
        适用多选下拉框
        :param elementInfo:
        :param values:以数组传参
        :return:
        """
        webElement= Select(self.getElement(elementInfo))
        webElement.deselect_all()
        for value in values:
            webElement.select_by_value(value)

    def select_dropDownBox_by_texts(self,elementInfo,texts):
        """
        适用多选下拉框
        :param elementInfo:
        :param texts:以数组传参
        :return:
        """
        webElement= Select(self.getElement(elementInfo))
        webElement.deselect_all()
        for text in texts:
            webElement.select_by_visible_text(text)

    def select_dropDownBox_by_indexs(self,elementInfo,indexs):
        """
        适用多选下拉框，下标从0开始
        :param elementInfo:
        :param indexs: 以数组传参
        :return:
        """
        webElement= Select(self.getElement(elementInfo))
        webElement.deselect_all()
        for index in indexs:
            webElement.select_by_index(index)

    def switch_to_window(self,window_name):
        self._driver.switch_to.window(window_name)

    def switch_to_frame(self,frame_name):
        self._driver.switch_to.frame(frame_name)

    def page_forward(self):
        self._driver.forward()

    def pag_back(self):
        self._driver.back()

    def dismiss_alert(self):
        alert=self._driver.switch_to.alert
        alert.dismiss()

    def accept_alert(self):
        alert=self._driver.switch_to.alert
        alert.accept()

    def get_alert_test(self):
        alert=self._driver.switch_to.alert
        return alert.text

    def get_screenshot(self,fileName):
        fileName=DateTimeTool.getNowTime('%Y%m%d%H%M%S%f_')+fileName
        allure.MASTER_HELPER.attach(fileName,self._driver.get_screenshot_as_png(),allure.MASTER_HELPER.attach_type.PNG)

    def getElement(self,elementInfo):
        """
        定位元素，包括需要等待定位和无需等待定位
        :param elementInfo:
        :return:
        """
        webElement=None
        locator_type=elementInfo.locator_type
        locator_value=elementInfo.locator_value
        wait_type = elementInfo.wait_type
        wait_seconds = elementInfo.wait_seconds
        wait_expected_value = elementInfo.wait_expected_value
        if wait_expected_value:
            wait_expected_value = wait_expected_value.decode('utf-8')
        # 需等待元素定位
        if wait_type:
            if wait_type == Wait_By.TITLE_IS:
                webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.title_is(wait_expected_value))
            elif wait_type == Wait_By.TITLE_CONTAINS:
                webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.title_contains(wait_expected_value))
            elif wait_type == Wait_By.PRESENCE_OF_ELEMENT_LOCATED:
                webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.presence_of_element_located((locator_type, locator_value)))
            elif wait_type == Wait_By.ELEMENT_TO_BE_CLICKABLE:
                webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.element_to_be_clickable((locator_type, locator_value)))
            elif wait_type == Wait_By.ELEMENT_LOCATED_TO_BE_SELECTED:
                webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.element_located_to_be_selected((locator_type, locator_value)))
            elif wait_type == Wait_By.VISIBILITY_OF:
                if locator_type == By.ID:
                    webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.visibility_of(self._driver.find_element_by_id(locator_value)))
                elif locator_type == By.NAME:
                    webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.visibility_of(self._driver.find_element_by_name(locator_value)))
                elif locator_type == By.LINK_TEXT:
                    webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.visibility_of(self._driver.find_element_by_link_text(locator_value)))
                elif locator_type == By.XPATH:
                    webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.visibility_of(self._driver.find_element_by_xpath(locator_value)))
                elif locator_type == By.PARTIAL_LINK_TEXT:
                    # 部分链接文本
                    webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.visibility_of(self._driver.find_element_by_partial_link_text(locator_value)))
                elif locator_type == By.CSS_SELECTOR:
                    webElement = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.visibility_of(self._driver.find_element_by_css_selector(locator_value)))
            return webElement

        # 无需等待元素定位
        if locator_type==By.ID:
            webElement=self._driver.find_element_by_id(locator_value)
        elif locator_type==By.NAME:
            webElement=self._driver.find_element_by_name(locator_value)
        elif locator_type==By.LINK_TEXT:
            webElement=self._driver.find_element_by_link_text(locator_value)
        elif locator_type==By.XPATH:
            webElement=self._driver.find_element_by_xpath(locator_value)
        elif locator_type==By.PARTIAL_LINK_TEXT:
            # 部分链接文本
            webElement=self._driver.find_element_by_partial_link_text(locator_value)
        elif locator_type==By.CSS_SELECTOR:
            webElement=self._driver.find_element_by_css_selector(locator_value)
        return webElement

    def getDriver(self):
        return self._driver

    def close(self):
        self._driver.__exit__()
