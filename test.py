# -*- coding: UTF-8 -*-
import os
import requests
from datetime import datetime

url = 'http://www.sfrtravel.com/'
res = requests.get(url)
if (res.status_code != 200):
"""
    os.system("ls")
    os.system("killall php-fpm")
    os.system("/usr/local/bin/php-fpm")
    comment = 'echo "%s restart php-fpm" >> /home/louis/log/fpm.log' % restart_time
    os.system(comment)
"""
