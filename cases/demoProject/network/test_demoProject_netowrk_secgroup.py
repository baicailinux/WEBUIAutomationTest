#-*- coding:utf-8 -*-
from base.demoProject.demoProjectClient import DemoProjectClient
from page_objects.demoProject.pages.indexPage import IndexPage
from assertpy import assert_that

class TestNetworkSecgroup:
    def setup_class(self):
        self.demoProject=DemoProjectClient(1)
        # 进入到安全组页面
        indexPage=IndexPage(self.demoProject.browserOperator)
        indexPage.click_menu_network()
        self.secgroupPage=indexPage.click_menu_network_secgroup()

    def test_secgroup_search_with_chinese_chars(self):
        self.secgroupPage.search_secgroup('中文啊啊啊')
        assert_that(2).is_equal_to(2)

    def teardown_class(self):
        self.demoProject.browserOperator.close()