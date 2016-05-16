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
    dirver.get("http://login.qyer.com/login.php")
    time.sleep(1)
    dirver.find_element_by_name('mail_input').send_keys(name)
    dirver.find_element_by_name('password').send_keys(password)
    #dirver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/input').click()

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
    
    logging = tool.log_init(model="a", file_name="qy_add_comment")
    name.append(settings.qy_login['ipiaoling']['name'])
    password.append(settings.qy_login['ipiaoling']['password'])
    url.append(u'http://bbs.qyer.com/thread-1080132-1.html')
    text.append( u'巴黎,尼斯,普罗旺斯,勃艮第,波尔多等法国自由行路线设计 欢迎咨询预订！或者直接拨打电话：40084-50085 !')
    i = 0
    dirver = init()
    time.sleep(2)
    login(dirver, name[i], password[i])
    time.sleep(20)
    while True:
        try:
            comment(dirver, url[i], text[i])
        except:
            logging.info('the program has some problems, and it will restart after 1h')
            mem_free = meminfo('MemFree')
            logging.info("Free memory:{0}".format(mem_free))
            """
            #answer = raw_input("Do you want to restart this program ? ")
            #if answer.strip() in "y Y yes Yes YES".split():
            logging.info('the program has some problems, and it will restart after 1h')
            mem_free = meminfo('MemFree')
            logging.info("Free memory:{0}".format(mem_free))
            time.sleep(3600)
            tool.restart_program()
            """
        time.sleep(10800)
