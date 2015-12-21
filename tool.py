# -*- coding:utf-8 -*-
import logging
import os
import sys
from datetime import datetime

def log_init(file_name=""):
    today = datetime.now()
    time_tmp = str(today).split(" ")
    timestamp = time_tmp[0]+"_"+time_tmp[1].split(".")[0]+"_"
    logging.basicConfig(
        filename=os.path.join(os.getcwd(), "log-txt/"+timestamp+file_name+".txt"),
        level=logging.INFO,
        filemode="w",
        format='%(asctime)s - %(levelname)s: %(message)s'
    )
    return logging
  
def restart_program():
    """Restarts the current program. 
    Note: this function does not return. Any cleanup action (like 
    saving data) must be done before calling this function."""  
    python = sys.executable  
    os.execl(python, python, * sys.argv)