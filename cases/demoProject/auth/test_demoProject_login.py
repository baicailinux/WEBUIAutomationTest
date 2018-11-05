# -*- coding:utf8 -*-
from assertpy import assert_that
from base.demoProject.demoProjectClient import DemoProjectClient
from page_objects.demoProject.pages.loginPage import LoginPage
import pytest
class TestLogin:

    def setup_class(self):
        self.demoProjectClient=DemoProjectClient()
        self.loginPage=LoginPage(self.demoProjectClient.browserOperator)

    def test_empty_username_and_empty_password(self):
        self.loginPage.loginFail('', '')
        assert_that(self.demoProjectClient.browserOperator.getText(
            self.loginPage.getElements().loginEmptyUsernameAndPassword_password_tip)).is_equal_to(
            self.loginPage.getElements().loginEmptyUsernameAndPassword_password_tip.expected_value)
        assert_that(self.demoProjectClient.browserOperator.getText(
            self.loginPage.getElements().loginEmptyUsernameAndPassword_username_tip)).is_equal_to(
            self.loginPage.getElements().loginEmptyUsernameAndPassword_username_tip.expected_value)

    def test_empty_username(self):
        self.loginPage.loginFail('','123456')
        assert_that(self.demoProjectClient.browserOperator.getText(
            self.loginPage.getElements().loginEmptyUsername_tip)).is_equal_to(
            self.loginPage.getElements().loginEmptyUsername_tip.expected_value)

    def test_empty_password(self):
        self.loginPage.loginFail('admin', '')
        assert_that(self.demoProjectClient.browserOperator.getText(
            self.loginPage.getElements().loginEmptyPassword_tip)).is_equal_to(
            self.loginPage.getElements().loginEmptyPassword_tip.expected_value)

    def test_login_success(self):
        indexPage=self.loginPage.loginSuccess('zpyadmin','123456..')
        assert_that(self.demoProjectClient.browserOperator.getTitle()).is_equal_to(indexPage.getElements().title.wait_expected_value)

    def teardown_class(self):
        self.demoProjectClient.browserOperator.close()