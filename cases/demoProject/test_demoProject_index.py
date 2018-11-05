# -*- coding:utf8 -*-
from base.demoProject.demoProjectClient import DemoProjectClient
from page_objects.demoProject.pages.indexPage import IndexPage
class TestIndex:
    def setup_class(self):
        self.demoProjectClient = DemoProjectClient(1)
        self.indexPage=IndexPage(self.demoProjectClient.browserOperator)

    def test_click_secgroup_menu(self):
        self.indexPage.click_menu_network()
        self.indexPage.click_menu_network_secgroup()

    def teardown_class(self):
        self.demoProjectClient.browserOperator.close()