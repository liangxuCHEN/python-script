#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import settings
import tool
from meminformation import meminfo

def init():
    dirver = webdriver.Firefox()
    return dirver

def login(dirver, name, password):
    dirver.get("https://mail.sina.com.cn/register/regmail.php")
    time.sleep(1)
    dirver.find_element_by_name('email').send_keys(name)
    dirver.find_element_by_name('psw').send_keys(password)

if __name__ == "__main__":
    logging = tool.log_init(file_name="sina_email")
    password = "qi0658214120"
    i = 5
    while i:
        dirver = init()
        time.sleep(2)
        name = str(time.time()).split(".")[0] + "_" + str(i)
        print name
        logging.info("name : " + name + " ; password: " + password)
        login(dirver, name, password)
        i = i -1
