#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import os
import sys
import settings
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
    dirver.get("http://login.qyer.com/login.php")
    time.sleep(1)
    dirver.find_element_by_name('mail_input').send_keys(name)
    dirver.find_element_by_name('password').send_keys(password)
    dirver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/input').click()

#dirver.get('http://bbs.qyer.com/thread-785994-1.html')
def comment(dirver, url,  text):
    dirver.get(url)
    time.sleep(4)
    dirver.find_element_by_id('topicReplyDefault').click()
    js_script = """
    var f = document.getElementById("topicReplyEditor").getElementsByTagName('iframe')[0];
    var doc = f.contentWindow.document;
    doc.body.innerHTML ="<p>""" + text + '</p>";'
    dirver.execute_script(js_script)
    button = dirver.find_element_by_xpath("//div[@id='topicReplyEditor']//input")
    button.click()

if __name__ == "__main__":
    name = []
    password = []
    url = []
    text = []
    
    name.append(settings.qy_login['ipiaoling']['name'])
    password.append(settings.qy_login['ipiaoling']['password'])
    url.append(u'http://bbs.qyer.com/thread-1080132-1.html')
    name.append(settings.qy_login['europely']['name'])
    password.append(settings.qy_login['europely']['password'])
    url.append(u'http://bbs.qyer.com/thread-1079156-1.html')

    text.append( u'巴黎,尼斯,普罗旺斯,勃艮第,波尔多等法国自由行路线设计 欢迎咨询预订！或者直接拨打电话：40084-50085 !')
    text.append( u'欧洲各国长线多日游路线设计高端定制游,婚纱/蜜月/休闲/购物高端定制,高尔夫/热气球/游轮/酒庄等高端商务旅游定制,展览展会组织接待,欢迎咨询预订！客服QQ:1372482437')
    i = 0
    while True:
        try:
            dirver = init()
            time.sleep(2)
            login(dirver, name[i], password[i])
            time.sleep(6)
            comment(dirver, url[i], text[i])
            dirver.close()
        except:
            #answer = raw_input("Do you want to restart this program ? ")
            #if answer.strip() in "y Y yes Yes YES".split():
            print 'the program has some problems, and it will restart after 1h'
            mem_free = meminfo('MemFree')
            print("Free memory:{0}".format(mem_free))
            time.sleep(3600)
            restart_program()
        
        time.sleep(10800)
        i = (1+i) % 2

