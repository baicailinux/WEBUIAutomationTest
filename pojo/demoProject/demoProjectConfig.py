# -*- coding:utf-8 -*-
class DemoProjectConfig:
    def __init__(self):
        self.browser_type = None
        self.web_host = None
        self.mysql_server = None
        self.mysql_port = None
        self.mysql_username = None
        self.mysql_password = None
        self.normal_username = None
        self.normal_password = None

    @property
    def browser_type(self):
        return self.browser_type

    @browser_type.setter
    def browser_type(self,browser_type):
        self.browser_type=browser_type

    @property
    def web_host(self):
        return self.web_host

    @web_host.setter
    def web_host(self,web_host):
        self.web_host=web_host

    @property
    def mysql_server(self):
        return self.mysql_server

    @mysql_server.setter
    def mysql_server(self, mysql_server):
        self.mysql_server = mysql_server

    @property
    def mysql_port(self):
        return self.mysql_port

    @mysql_port.setter
    def mysql_port(self, mysql_port):
        self.mysql_port = mysql_port

    @property
    def mysql_username(self):
        return self.mysql_username

    @mysql_username.setter
    def mysql_username(self, mysql_username):
        self.mysql_username = mysql_username

    @property
    def mysql_password(self):
        return self.mysql_password

    @mysql_password.setter
    def mysql_password(self, mysql_password):
        self.mysql_password = mysql_password

    @property
    def normal_username(self):
        return self.normal_username

    @normal_username.setter
    def normal_username(self,normal_username):
        self.normal_username=normal_username