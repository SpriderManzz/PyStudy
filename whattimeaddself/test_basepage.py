# coding=utf-8
import time
from selenium import webdriver
from whattimeaddself.basepage import BasePage


class OpenUrl(object):
    driver = webdriver.Firefox()
    basepage = BasePage(driver)

    def open_url(self):
        self.basepage.open_url("https://www.baidu.com")

op = OpenUrl()
op.open_url()

