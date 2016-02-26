# -*- coding:utf-8 -*-
import httplib2
import tool
#re  request
URL = "http://127.0.0.1:8000/check_bill"
#log init
logging = tool.log_init(file_name="check_bill_log")
logging.info("******misson  begin*****" )
#init
h = httplib2.Http()
res,content = h.request(URL, "GET")
logging.info(content.decode("utf-8"))
logging.info(u"============End ========="  )



