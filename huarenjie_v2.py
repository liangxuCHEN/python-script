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
    
    max_len = len(settings.huarenjie_url)
    i = 0
    count_error = 0
    while True:
        try:
            dirver = init()
            time.sleep(2)
            login(dirver, settings.huarenjie_url[i]["name"], settings.huarenjie_url[i]["password"])
            time.sleep(6)
            comment(dirver, settings.huarenjie_url[i]["url"], settings.huarenjie_url[i]["text"])
            dirver.close()
            print (settings.huarenjie_url[i]["url"])
            i = (i+1) % max_len
            count_error = 0
        except:
            #answer = raw_input("Do you want to restart this program ? ")
            #if answer.strip() in "y Y yes Yes YES".split():
            count_error = count_error + 1
            if count_error < 10:
                print('the program has some problems, it will try again after few minuites, it is %d time' % count_error )
            else:
                 print('the program will restart')
                 time.sleep(3600)
                 tool.restart_program()
            #mem_free = meminfo('MemFree')
            #logging.info("Free memory:{0}".format(mem_free))
            time.sleep(800)
            
        time.sleep(1500)
