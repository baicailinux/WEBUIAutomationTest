# -*- coding:utf-8 -*-
from pojo.demoProject.demoProjectConfig import DemoProjectConfig
import ConfigParser

class DemoProjectReadConfig(object):
    __instance=None
    __inited=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__inited is None:
            self.config=self._readConfig('config/demoProject/demoProject.conf')
            self.__inited=True

    def _readConfig(self, configFile):
        config = ConfigParser.ConfigParser()
        config.read(configFile)
        demoProjectConfig = DemoProjectConfig()
        demoProjectConfig.browser_type = config.get('browsers', 'browser_type')
        demoProjectConfig.web_host = config.get('servers','web_host')
        demoProjectConfig.mysql_server = config.get('mysql', 'mysql_server')
        demoProjectConfig.mysql_port = config.get('mysql', 'mysql_port')
        demoProjectConfig.mysql_username = config.get('mysql', 'mysql_username')
        demoProjectConfig.mysql_password = config.get('mysql', 'mysql_password')
        demoProjectConfig.normal_username = config.get('users','normal_username')
        demoProjectConfig.normal_password = config.get('users', 'normal_password')
        return demoProjectConfig
