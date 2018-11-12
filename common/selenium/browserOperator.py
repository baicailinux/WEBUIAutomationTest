#-*- coding:utf8 -*-
from common.dateTimeTool import DateTimeTool
from pojo.elementInfo import ElementInfo
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from page_objects.wait_type import Wait_Type  as Wait_By
import allure
import os

class BrowserOperator:
    """
    类中的element参数可以有selenium.webdriver.remote.webelement.WebElement和pojo.elementInfo.ElementInfo类型
    """

    def __init__(self,driver):
        self._driver=driver

    def get(self,url):
        self._driver.get(url)

    def get_current_url(self):
        return self._driver.current_url.encode('utf-8')

    def getTitle(self):
        return self._driver.title.encode('utf-8')

    def getText(self,element):
        if isinstance(element, ElementInfo):
            webElement=self.getElement(element)
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        return webElement.text.encode('utf-8')

    def click(self,element):
        if isinstance(element, ElementInfo):
            webElement=self.getElement(element)
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        webElement.click()

    def sendText(self,element,text):
        text=text.decode('utf-8')
        if isinstance(element, ElementInfo):
            webElement=self.getElement(element)
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        webElement.clear()
        webElement.send_keys(text)

    def is_displayed(self,element):
        if isinstance(element, ElementInfo):
            webElement=self.getElement(element)
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        flag=webElement.is_displayed()
        return flag

    def is_enabled(self,element):
        if isinstance(element, ElementInfo):
            webElement = self.getElement(element)
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        flag = webElement.is_enabled()
        return flag

    def is_selected(self,element):
        if isinstance(element, ElementInfo):
            webElement = self.getElement(element)
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        flag = webElement.is_selected()
        return flag

    def select_dropDownBox_by_value(self,element,value):
        """
        适用单选下拉框
        :param webElement:
        :param value:
        :return:
        """
        if isinstance(element, ElementInfo):
            webElement = Select(self.getElement(element))
        elif isinstance(element,WebElement):
            webElement=Select(element)
        else:
            return None
        webElement.select_by_value(value)

    def select_dropDownBox_by_text(self,element,text):
        """
        适用单选下拉框
        :param webElement:
        :param text:
        :return:
        """
        if isinstance(element, ElementInfo):
            webElement= Select(self.getElement(element))
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        webElement.select_by_visible_text(text)

    def select_dropDownBox_by_index(self,element,index):
        """
        适用单选下拉框,下标从0开始
        :param webElement:
        :param index:
        :return:
        """
        if isinstance(element, ElementInfo):
            webElement= Select(self.getElement(element))
        elif isinstance(element,WebElement):
            webElement=element
        else:
            return None
        webElement.select_by_index(index)

    def select_dropDownBox_by_values(self,element,values):
        """
        适用多选下拉框
        :param webElement:
        :param values:以数组传参
        :return:
        """
        if isinstance(element, ElementInfo):
            webElement = Select(self.getElement(element))
        elif isinstance(element, WebElement):
            webElement = Select(element)
        else:
            return None
        webElement.deselect_all()
        for value in values:
            webElement.select_by_value(value)

    def select_dropDownBox_by_texts(self,element,texts):
        """
        适用多选下拉框
        :param webElement:
        :param texts:以数组传参
        :return:
        """
        if isinstance(element, ElementInfo):
            webElement = Select(self.getElement(element))
        elif isinstance(element, WebElement):
            webElement = Select(element)
        else:
            return None
        webElement.deselect_all()
        for text in texts:
            webElement.select_by_visible_text(text)

    def select_dropDownBox_by_indexs(self,element,indexs):
        """
        适用多选下拉框，下标从0开始
        :param webElement:
        :param indexs: 以数组传参
        :return:
        """
        if isinstance(element, ElementInfo):
            webElement = Select(self.getElement(element))
        elif isinstance(element, WebElement):
            webElement = Select(element)
        else:
            return None
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

    def refresh(self):
        self._driver.refresh()

    def uploadFile(self,element,filePath):
        """
        适用于元素为input且type="file"的文件上传
        :param webElement:
        :param filePath:
        :return:
        """
        if isinstance(element, ElementInfo):
            webElement = self.getElement(element)
        elif isinstance(element,WebElement):
            webElement = element
        else:
            return None
        webElement.send_keys(os.path.abspath(filePath))

    def get_property(self,element,property_name):
        if isinstance(element, ElementInfo):
            webElement = self.getElement(element)
        elif isinstance(element,WebElement):
            webElement = element
        else:
            return None
        return webElement.get_property(property_name)

    def get_attribute(self,element,attribute_name):
        if isinstance(element, ElementInfo):
            webElement = self.getElement(element)
        elif isinstance(element,WebElement):
            webElement = element
        else:
            return None
        return webElement.get_attribute(attribute_name)

    def get_element_outer_html(self,element):
        return self.get_attribute(element,'outerHTML')

    def get_element_inner_html(self, element):
        return self.get_attribute(element,'innerHTML')

    def get_table_data(self,element,data_type='text'):
        """
        以二维数组返回表格每一行的每一列的数据[[row1][row2][colume1,clume2]]
        :param webElement:
        :param data_type: text-返回表格文本内容,html-返回表格html内容
        :return:
        """
        if isinstance(element, ElementInfo):
            # 由于表格定位经常会出现【StaleElementReferenceException: Message: stale element reference: element is not attached to the page document 】异常错误,
            # 解决此异常只需要用显示等待，保证元素存在即可，显示等待类型中VISIBILITY_OF有实现StaleElementReferenceException异常捕获,
            # 所以强制设置表格定位元素时使用VISIBILITY_OF
            element.wait_type=Wait_By.VISIBILITY_OF
            webElement = self.getElement(element)
        elif isinstance(element,WebElement):
            webElement = element
        else:
            return None
        table_trs = webElement.find_elements_by_tag_name('tr')
        table_data=[]
        for tr in table_trs:
            tr_data=[]
            # 此处同样用于解决StaleElementReferenceException异常问题
            WebDriverWait(self._driver,30).until(expected_conditions.visibility_of(tr))
            tr_tds = tr.find_elements_by_tag_name('td')
            if data_type.lower()=='text':
                for td in tr_tds:
                    tr_data.append(td.text)
            elif data_type.lower()=='html':
                for td in tr_tds:
                    tr_data.append(td.get_attribute('innerHTML'))
            table_data.append(tr_data)
        return table_data

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
                webElements = WebDriverWait(self._driver,wait_seconds).until((expected_conditions.visibility_of_all_elements_located((locator_type,locator_value))))
                if len(webElements)>0:
                    webElement=webElements[0]
        else:
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
            elif locator_type==By.CLASS_NAME:
                webElement = self._driver.find_element_by_class_name(locator_value)
            elif locator_type==By.TAG_NAME:
                webElement = self._driver.find_element_by_tag_name(locator_value)
        if isinstance(webElement,WebElement):
            # 此处同样用于解决StaleElementReferenceException异常问题
            WebDriverWait(self._driver,30).until(expected_conditions.visibility_of(webElement))
            self.highLight(webElement)
        return webElement

    def getElements(self,elementInfo):
        """
        定位多个元素
        :param elementInfo:
        :return:
        """
        webElements=None
        locator_type=elementInfo.locator_type
        locator_value=elementInfo.locator_value
        wait_type = elementInfo.wait_type
        wait_seconds = elementInfo.wait_seconds
        # 需等待元素定位
        if wait_type:
            if wait_type == Wait_By.PRESENCE_OF_ELEMENT_LOCATED:
                webElements = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.presence_of_all_elements_located((locator_type, locator_value)))
            elif wait_type == Wait_By.VISIBILITY_OF:
                webElements = WebDriverWait(self._driver, wait_seconds).until(expected_conditions.visibility_of_all_elements_located((locator_type,locator_value)))
        else:
            # 无需等待元素定位
            if locator_type==By.ID:
                webElements=self._driver.find_elements_by_id(locator_value)
            elif locator_type==By.NAME:
                webElements=self._driver.find_elements_by_name(locator_value)
            elif locator_type==By.LINK_TEXT:
                webElements=self._driver.find_elements_by_link_text(locator_value)
            elif locator_type==By.XPATH:
                webElements=self._driver.find_elements_by_xpath(locator_value)
            elif locator_type==By.PARTIAL_LINK_TEXT:
                # 部分链接文本
                webElements=self._driver.find_elements_by_partial_link_text(locator_value)
            elif locator_type==By.CSS_SELECTOR:
                webElements=self._driver.find_elements_by_css_selector(locator_value)
            elif locator_type==By.CLASS_NAME:
                webElements = self._driver.find_elements_by_class_name(locator_value)
            elif locator_type==By.TAG_NAME:
                webElements =  self._driver.find_elements_by_tag_name(locator_value)
        for webElement in webElements:
            if isinstance(webElement, WebElement):
                # 此处同样用于解决StaleElementReferenceException异常问题
                WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of(webElement))
                self.highLight(webElement)
        return webElements

    def getSubElement(self,parent_element,sub_elementInfo):
        """
        获得元素的子元素
        :param parent_element: 父元素
        :param sub_elementInfo: 子元素,只能提供pojo.elementInfo.ElementInfo类型
        :return:
        """
        if isinstance(parent_element,ElementInfo):
            webElement=self.getElement(parent_element)
        elif isinstance(parent_element,WebElement):
            webElement=parent_element
        else:
            return None
        if not isinstance(sub_elementInfo,ElementInfo):
            return None
        # 此处同样用于解决StaleElementReferenceException异常问题
        WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of(webElement))
        # 通过父元素查找子元素
        locator_type=sub_elementInfo.locator_type
        locator_value=sub_elementInfo.locator_value
        if locator_type == By.ID:
            subWebElement =webElement.find_element_by_id(locator_value)
        elif locator_type == By.NAME:
            subWebElement = webElement.find_element_by_name(locator_value)
        elif locator_type == By.LINK_TEXT:
            subWebElement = webElement.find_element_by_link_text(locator_value)
        elif locator_type == By.XPATH:
            subWebElement = webElement.find_element_by_xpath(locator_value)
        elif locator_type == By.PARTIAL_LINK_TEXT:
            subWebElement = webElement.find_element_by_partial_link_text(locator_value)
        elif locator_type == By.CSS_SELECTOR:
            subWebElement = webElement.find_element_by_css_selector(locator_value)
        elif locator_type == By.CLASS_NAME:
            subWebElement = webElement.find_element_by_class_name(locator_value)
        elif locator_type == By.TAG_NAME:
            subWebElement = webElement.find_element_by_tag_name(locator_value)
        else:
            return None
        if isinstance(subWebElement,WebElement):
            # 此处同样用于解决StaleElementReferenceException异常问题
            WebDriverWait(self._driver,30).until(expected_conditions.visibility_of(subWebElement))
            self.highLight(subWebElement)
        return subWebElement

    def getSubElements(self, parent_element, sub_elementInfo):
        """
        获得元素的多个子元素
        :param parent_element: 父元素
        :param sub_elementInfo: 子元素,只能提供pojo.elementInfo.ElementInfo类型
        :return:
        """
        if isinstance(parent_element,ElementInfo):
            webElement=self.getElement(parent_element)
        elif isinstance(parent_element,WebElement):
            webElement=parent_element
        else:
            return None
        if not isinstance(sub_elementInfo,ElementInfo):
            return None
        # 此处同样用于解决StaleElementReferenceException异常问题
        WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of(webElement))
        # 通过父元素查找多个子元素
        locator_type = sub_elementInfo.locator_type
        locator_value = sub_elementInfo.locator_value
        if locator_type == By.ID:
            subWebElements = webElement.find_elements_by_id(locator_value)
        elif locator_type == By.NAME:
            subWebElements = webElement.find_elements_by_name(locator_value)
        elif locator_type == By.LINK_TEXT:
            subWebElements = webElement.find_elements_by_link_text(locator_value)
        elif locator_type == By.XPATH:
            subWebElements = webElement.find_elements_by_xpath(locator_value)
        elif locator_type == By.PARTIAL_LINK_TEXT:
            subWebElements = webElement.find_elements_by_partial_link_text(locator_value)
        elif locator_type == By.CSS_SELECTOR:
            subWebElements = webElement.find_elements_by_css_selector(locator_value)
        elif locator_type == By.CLASS_NAME:
            subWebElements = webElement.find_elements_by_class_name(locator_value)
        elif locator_type == By.TAG_NAME:
            subWebElements = webElement.find_elements_by_tag_name(locator_value)
        else:
            return None
        for subWebElement in subWebElements:
            if isinstance(subWebElement, WebElement):
                # 此处同样用于解决StaleElementReferenceException异常问题
                WebDriverWait(self._driver, 30).until(expected_conditions.visibility_of(subWebElement))
                self.highLight(subWebElement)
        return subWebElements

    def explicit_wait_page_title(self,elementInfo):
        """
        显式等待页面title
        :param elementInfo:
        :return:
        """
        self.getElement(elementInfo)

    def highLight(self,webElement,seconds=5):
        self._driver.execute_script("element = arguments[0];" +
                              "original_style = element.getAttribute('style');" +
                              "element.setAttribute('style', original_style + \";" +
                              " border: 3px dashed rgb(250,0,255);\");" +
                              "setTimeout(function(){element.setAttribute('style', original_style);}, "+str(seconds*1000)+");",
                                    webElement)

    def getDriver(self):
        return self._driver

    def close(self):
        self._driver.__exit__()
