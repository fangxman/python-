#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#filename:log_mode.py
#author:man


"""
帮助
"""
def __help__():
	print("函数说明".center(70,"-"))
	print("__help__				=>		帮助")
	print("open_file			=>		打开日志文件")
	print("close_file			=>		关闭日志文件")
	print("print_log			=>		打印日志内容")
	print("read_log				=>		读取日志内容")
	
"""
打开日志文件
filepath:日志文件的路径
"""
def open_file(filepath):
	return open(filepath,"w+")

"""
#关闭日志文件	
file:打开的日志文件
"""
def close_file(file):
	file.close()
	
"""
#打印日志内容
file:打开的日志文件
text:打印到日志的内容
"""
def print_log(file,text):
	file.write(text)
	
"""
#读取日志内容
file:打开的日志文件
num:需要读取的日志的前几行
"""
def read_log(file,num):
	return file.read(num)
	
if __name__ == "__main__":
	__help__()