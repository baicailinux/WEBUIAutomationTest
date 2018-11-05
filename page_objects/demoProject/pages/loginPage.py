#-*- coding:utf-8 -*-
from page_objects.demoProject.elements.loginPageElements import LoginPageElements
from page_objects.demoProject.pages.indexPage import IndexPage
class LoginPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._loginPageElements=LoginPageElements()
        self._browserOperator.implicity_wait(self._loginPageElements.title)

    def loginSuccess(self,username,password):
        self._browserOperator.sendText(self._loginPageElements.usernameInput,username)
        self._browserOperator.sendText(self._loginPageElements.passwordInput,password)
        self._browserOperator.click(self._loginPageElements.loginBtn)
        self._browserOperator.get_screenshot('loginSuccess')
        return IndexPage(self._browserOperator)

    def loginFail(self,username,password):
        self._browserOperator.sendText(self._loginPageElements.usernameInput, username)
        self._browserOperator.sendText(self._loginPageElements.passwordInput, password)
        self._browserOperator.click(self._loginPageElements.loginBtn)
        self._browserOperator.get_screenshot('loginFail')

    def getElements(self):
        return self._loginPageElements