# -*- coding:utf-8 -*-
#!/usr/bin/python
import httplib2
import tool
#re  request
URL = "http://112.74.109.3:4040/check_bill"
#log init
logging = tool.log_init(model="a", file_name="check_bill_log")
logging.info("******misson  begin*****" )
#init
h = httplib2.Http()
res,content = h.request(URL, "GET")
logging.info(content.decode("utf-8"))
logging.info(u"============End ========="  )



