# -*- coding:utf-8 -*-
from requests.auth import HTTPDigestAuth
import requests
import json
import re

REGER_hash = 'formhash".+>'
REGER_URL = 'action=".+" '
"""
name = u"法国飘零旅游"
password = "qi77689377"
#auth = HTTPBasicAuth(name, password)
auth = HTTPDigestAuth(name, password)
url = "http://www.huarenjie.com/forum.php?mod=post&action=reply&fid=664&tid=5296279&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"
login_url = "http://www.huarenjie.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LlJa8&inajax=1"
body = json.dumps({
    u"message" : u"酒庄参观四季皆宜，有打算去波尔多的童鞋，联系我们吧",
    "formhash" : "46d605b4",
})
res = requests.post(url=url, data=body, auth=auth)

url = "http://www.huarenjie.com/forum.php?mod=post&action=reply&fid=664&tid=5296279&extra=page%3D1&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1"


"""

s = requests.Session()
data = {
    "formhash":"e19a5978",
    "referer":"http://www.huarenjie.com/thread-5296279-32-1.html",
    "username":u"环欧洲旅游",
    "password":"3612235Qq",
    "questionid":"0",
    "answer":"",
    "cookietime":"2592000",
}

url = 'http://www.huarenjie.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LlJa8&inajax=1'

res = s.post(url=url, data=data)
print res.content
print res.status_code

url = "http://www.huarenjie.com/thread-6177618-1-1.html"
res = requests.get(url=url)
print res.status_code

result = re.findall(REGER_hash, res.content.decode("utf-8"))
print result
formhash = result[0][-12:-4]
print formhash

result = re.findall(REGER_URL, res.content)

prama = result[0][8:-2].replace('&amp;','&')

url = "http://www.huarenjie.com/forum.php"
print url

data_param = {
    "mod":"post",
    "action":"reply",
    "fid":"664",
    "tid":"5296279",
    "extra":"page%3D1",
    "replysubmit":"yes",
    "infloat":"yes",
    "handlekey":"fastpost",
    "inajax":"1",
}

message = {
    "message" : u"酒庄参观四季皆宜，有打算去波尔多的童鞋，联系我们吧",
    "formhash" : formhash,
    "usesig":"",
    "subject":"  ",
}
head_info = {
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"www.huarenjie.com",
    "Origin":"http://www.huarenjie.com",
    "Referer":"http://www.huarenjie.com/thread-5296279-32-1.html",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
}
res = s.post(url=url, data=message, params=data_param)
print res.status_code
print res.content