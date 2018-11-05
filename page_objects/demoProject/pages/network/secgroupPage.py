#-*- coding:utf-8 -*-
from page_objects.demoProject.elements.network.secgroupPageElements import SecgroupPageElements
class SecgroupPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._secgroupPageElement=SecgroupPageElements()
        self._browserOperator.implicity_wait(self._secgroupPageElement.title)

    def search_secgroup(self,keyword):
        self._browserOperator.sendText(self._secgroupPageElement.search,keyword)
