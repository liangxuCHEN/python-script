#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import tool
import settings
from meminformation import meminfo

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
    
    logging = tool.log_init(model="a", file_name="huarenjie_comment")
    name.append(u'法国飘零旅游')
    password.append('qi77689377')
    url.append('http://www.huarenjie.com/thread-6224687-1-1.html')
    text.append( u'联系我们吧，飘零旅游竭诚为您服务 欢迎咨询预订！或者直接拨打电话：400-845-0085（中国）+336 50 09 91 78 (法国) ')

    url.append('http://www.huarenjie.com/thread-6177618-1-1.html')
    name.append(u'法国南法旅游')
    password.append('qi77689377')
    text.append( u'欢迎咨询预订,联系方式：官方网站：www.sfrtravel.com;联系电话：客服：+33 6 66 95 21 03 （8：00至20：00）;客服微信：nanfalvyou')
    
    name.append(u'环欧洲旅游')
    password.append('3612235Qq')
    url.append('http://www.huarenjie.com/thread-6203437-1-1.html')
    text.append( u'联系我们吧，欢迎咨询预订！或者直接拨打电话：+33662324159（法国） qq：1372482437 微信：1004745796 ')

    name.append(settings.huarenjie_login['0']['name'])
    password.append(settings.huarenjie_login['0']['password'])
    url.append('http://www.huarenjie.com/thread-5296279-1-1.html')
    text.append( u'酒庄参观四季皆宜，有打算去波尔多的童鞋，联系我们吧，飘零旅游竭诚为您服务 欢迎咨询预订！www.ipiaoling.com 或者直接拨打电话：+336 58 86 95 15 (法国) ')
    i = 0
    while True:
        try:
            dirver = init()
            time.sleep(2)
            login(dirver, name[i], password[i])
            time.sleep(6)
            comment(dirver, url[i], text[i])
            dirver.close()
            i = (i+1) % 4
        except:
            #answer = raw_input("Do you want to restart this program ? ")
            #if answer.strip() in "y Y yes Yes YES".split():
            print('the program has some problems' )
            #mem_free = meminfo('MemFree')
            #logging.info("Free memory:{0}".format(mem_free))
            time.sleep(800)
            #tool.restart_program()
        print i 
        time.sleep(4200)


