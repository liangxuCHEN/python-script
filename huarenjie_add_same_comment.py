#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os
import sys
from meminformation import meminfo

def restart_program():  
    """Restarts the current program. 
    Note: this function does not return. Any cleanup action (like 
    saving data) must be done before calling this function."""  
    python = sys.executable  
    os.execl(python, python, * sys.argv)

def init():
    dirver = webdriver.Firefox()
    return dirver

def login(dirver, name, password):
    dirver.get("http://www.huarenjie.com/member.php?mod=logging&action=login")
    time.sleep(15)
    dirver.find_element_by_name('username').send_keys(name)
    dirver.find_element_by_name('password').send_keys(password)
    dirver.find_element_by_name('loginsubmit').click()
    time.sleep(3)

#dirver.get('http://bbs.qyer.com/thread-785994-1.html')
def comment(dirver, url,  text):
    dirver.get(url)
    time.sleep(10)
    dirver.find_element_by_id('fastpostmessage').send_keys(text)
    dirver.find_element_by_id('fastpostsubmit').click()
    time.sleep(2)

if __name__ == "__main__":
    name = []
    password = []
    url = []
    text = []
    
    name.append(u'树上的鱼')
    password.append(u'p896959')
    url.append('http://www.huarenjie.com/thread-5296279-1-1.html')
    text.append( u'酒庄参观四季皆宜，有打算去波尔多的童鞋，联系我们吧，飘零旅游竭诚为您服务 欢迎咨询预订！或者直接拨打电话：400-845-0085（中国）+336 58 86 95 15 (法国) ')
    #i = 0
    while True:
        try:
            dirver = init()
            time.sleep(2)
            login(dirver, name[0], password[0])
            time.sleep(6)
            comment(dirver, url[0], text[0])
            dirver.close()
        except:
            #answer = raw_input("Do you want to restart this program ? ")
            #if answer.strip() in "y Y yes Yes YES".split():
            print 'the program has some problems, and it will restart after 1h'
            mem_free = meminfo('MemFree')
            print("Free memory:{0}".format(mem_free))
            time.sleep(3600)
            restart_program()
        
        #i = (i+1) % 2
        time.sleep(14400)


