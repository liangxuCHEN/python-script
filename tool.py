# -*- coding:utf-8 -*-
import logging
import os
import sys
from datetime import datetime

def log_init(model="", file_name=""):
    today = datetime.now()
    time_tmp = str(today).split(" ")
    timestamp = time_tmp[0]+"_"+time_tmp[1].split(".")[0]+"_"
    
    if (model == "a"):
        if not os.path.isfile("log-txt/"+file_name+".txt"):
            model = "w"
            file_name = timestamp + file_name
    else:
         model = "w"
         file_name = timestamp + file_name
    logging.basicConfig(
        filename=os.path.join(os.getcwd(), "log-txt/"+file_name+".txt"),
        level=logging.INFO,
        filemode=model,
        format='%(asctime)s - %(levelname)s: %(message)s'
    )
    return logging
  
def restart_program():
    """Restarts the current program. 
    Note: this function does not return. Any cleanup action (like 
    saving data) must be done before calling this function."""  
    python = sys.executable  
    os.execl(python, python, * sys.argv)