#-*- coding:utf-8 -*-
from page_objects.demoProject.elements.indexPageElements import IndexPageElements
from page_objects.demoProject.pages.network.secgroupPage import SecgroupPage
class IndexPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._indexPageElements=IndexPageElements()
        self._browserOperator.getElement(self._indexPageElements.title)

    def click_menu_network(self):
        self._browserOperator.click(self._indexPageElements.menu_network)
        self._browserOperator.get_screenshot('click_menu_network')

    def click_menu_network_secgroup(self):
        self._browserOperator.click(self._indexPageElements.menu_network_secgroup)
        self._browserOperator.get_screenshot('click_menu_network_secgroup')
        return SecgroupPage(self._browserOperator)

    def getElements(self):
        return self._indexPageElements