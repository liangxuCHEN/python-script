#_*_coding:utf8_*_
from __future__ import unicode_literals
import site; site.addsitedir("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages")
from lxml import etree
from lxml import html
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pyh import *


def getPage(page, end):
    driver = webdriver.Firefox()
    driver.get("http://www.csrwire.com/press_releases/"+str(page))
    time.sleep(1)
    titles=(driver.find_elements_by_xpath('//h3'))
    for title in titles:
        Title=str(title.text).encode('utf-8')
    companys=(driver.find_elements_by_xpath('//span[@class="green"]/a'))
    for company in companys:
        Company=str(company.text).encode('utf-8')
    categories=(driver.find_elements_by_xpath('//p[@class="loc"]/child::a'))
    for category in categories:
        Category=str(category.text).encode('utf-8')
    times=(driver.find_elements_by_xpath('//p[@class="loc"][2]'))
    for t in times:
        date = str(t.textContent).encode('utf-8')
        print date
    driver.close()
    #Table(Title, Company, Category)

def Table(Title, Company, Category):
    page =PyH('my site')
    page<<div(style="text-align:center")<<h4('Test table')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr1 = mytab << tr(bgcolor="lightgrey")
    tr1 <<th('Title')+th('Company')+th('Category')
    tr2 = mytab << tr()
    tr2<< td(Title)+td(Company)+td(Category)
    page.printOut('myTable.html')

pageStart=28999
pageEnd=28999
for page in range(pageStart,pageEnd+1):
    getPage(page,pageEnd)