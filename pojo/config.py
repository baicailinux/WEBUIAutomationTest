# -*- coding:utf-8 -*-
class Config:
    def __init__(self):
        self.selenium_hub=None
        self.test_workers=None

    @property
    def selenium_hub(self):
        return self.selenium_hub

    @selenium_hub.setter
    def selenium_hub(self,selenium_hub):
        self.selenium_hub=selenium_hub

    @property
    def test_workers(self):
        return self.test_workers

    @test_workers.setter
    def test_workers(self,test_workers):
        self.test_workers=test_workers
