#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#filename:time_mode.py
#author:man

import time
import calendar

"""
帮助
"""
def __help__():
	print ("函数说明".center(70,"-"))
	print ("__help__			=>		帮助")
	print ("get_now_time			=>		获取当前时间")
	print ("get_now_timestamp			=>		获取当前时间戳")
	
"""
获取当前时间
"""
def get_now_time():
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());

def get_now_timestamp():
	return calendar.timegm(time.gmtime());

if __name__ == "__main__":
	__help__()