# -*- coding:utf-8 -*-
import httplib2
#settings has the url of qy
import settings
import logging
import os
import re
import time
import sys
#re  request
NUM_READ = u"浏览数.([0-9]{1,})"

#init
len_post = len(settings.qy_url_list)
if len(sys.argv) > 1:
    ping_time = int(sys.argv[1]) * len_post
else:
    ping_time = len_post
num = {}
i = 0
logging.basicConfig(
    filename=os.path.join(os.getcwd(), 'log_qy.txt'),
    level=logging.DEBUG,
    filemode="a",
    format='%(asctime)s - %(levelname)s: %(message)s'
)
logging.info("******misson is  adding " + sys.argv[1] + " time reading count for each artical*****" )

h = httplib2.Http()
while ping_time:
    res,content = h.request(settings.qy_url_list[i], "GET")
    result = re.findall(NUM_READ, content.decode("utf-8"))
    if len(result) > 0 :
        num[i] =  result[0]
    i = (i+1) % len_post
    ping_time = ping_time - 1

logging.info(u"============Now 浏览数 ========="  )
for key,value in num.items():
    logging.info(value)

print "misson is finished " 



