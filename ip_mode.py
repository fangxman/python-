#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#filename:ip_mode.py
#author:man

import sys
import IPy
sys.path.append("/var/www/html/cloudmap_taihang/jiaoben/py_pack")
import tools_mode

"""
帮助
"""
def __help__():
	print ("函数说明".center(70,"-"))
	print ("__help__					=>		帮助")
	print ("IprangeToInt				=>		将单个IP范围拆分为整型")
	print ("IprangesToInt			=>		将多个IP范围拆分为整型")
	print ("get_access_iprange		=>		计算两个IP范围是否包含")


"""
将单个IP范围拆分为整型
iprange:IP范围
"""
def IprangeToInt(iprange):
	list_config=[]
	if('/' in iprange):
		ipstrs=iprange.split('/')
		base=IPy.IP('255.255.255.255').int()
		ip=IPy.IP(ipstrs[0]).int()
		mask=pow(2,32-int(ipstrs[1]))-1
		smask=mask ^ base
		min=ip & smask
		max=ip | mask
	elif('-' in iprange):
		ipstrs=iprange.split('-')
		min=IPy.IP(ipstrs[0]).int()
		max=IPy.IP(ipstrs[1]).int()
	else:
		min=max=IPy.IP(iprange).int()
	list_config.append(min);
	list_config.append(max);
	return list_config
	

"""
将多个IP范围拆分为整型
iprange:IP范围
"""
def IprangesToInt(iprange):
	iplist=[]
	#先验证该是否正确
	iprange=tools.check_ipranges(iprange)
	if iprange!="":
		if(',' in iprange):
			ipstrs=iprange.split(',')
			for ipstr in ipstrs:
				ipstr=IprangeToInt(ipstr)
				if ipstr :
					iplist.append(ipstr)
		elif(';' in iprange):
			ipstrs=iprange.split(';') 
			for ipstr in ipstrs:
				ipstr=IprangeToInt(ipstr)
				if ipstr :
					iplist.append(ipstr)
		else :
			ipstr=IprangeToInt(iprange)
			if ipstr :
				iplist.append(ipstr)
	return iplist
	
"""
计算两个IP范围是否包含
iprange1:IP范围
iprange2:IP范围
返回值:交叉的IP范围
"""
def get_access_iprange(iprange1s,iprange2s):
	iprange1s=IprangesToInt(iprange1s)
	iprange2s=IprangesToInt(iprange2s)
	iplist=[]
	for iprange1 in iprange1s:
		for iprange2 in iprange2s:
			if iprange1[0]>=iprange2[0] and iprange1[0]<=iprange2[1] and iprange1[1] >=iprange2[1]:
				iplist.append(iprange1[0])
				iplist.append(iprange2[1])
			elif iprange1[0]<=iprange2[0] and iprange2[0]<=iprange1[1] and iprange2[1]>=iprange1[1]:
				iplist.append(iprange2[0])
				iplist.append(iprange1[1])
			elif iprange1[0]>=iprange2[0] and iprange1[1]<=iprange2[1]:
				iplist.append(iprange1[0])
				iplist.append(iprange1[1])
			elif iprange2[0]>=iprange1[0] and iprange2[1]<=iprange1[1]:
				iplist.append(iprange2[0])
				iplist.append(iprange2[1])
	return iplist
	
if __name__ == "__main__":
	__help__()
		