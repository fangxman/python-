#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#filename:tools_mode.py
#author:man

import os
import IPy
import re
import urllib.parse
import base64

"""
帮助
"""
def __help__():
	print ("函数说明".center(70,"-"))
	print ("__help__				=>		帮助")
	print ("get_config				=>		格式化配置文件的内容")
	print ("ip_mask					=>		计算ip地址的掩码")
	print ("check_ip				=>		校验ip地址")
	print ("check_mac				=>		校验mac地址")
	print ("check_macs				=>		校验多个mac地址")
	print ("check_iprange				=>		校验单个ip范围")
	print ("check_ipranges				=>		校验多个ip范围")
	print ("check_email				=>		校验邮箱格式")
	print ("check_int				=>		校验是否整数")
	print ("check_date1				=>		校验是否日期")
	print ("check_date2				=>		校验是否日期")
	print ("check_datetime1				=>		校验是否日期时间")
	print ("check_datetime2				=>		校验是否日期时间")
	print ("check_datetime3				=>		校验是否日期时间")
	print ("check_datetime4				=>		校验是否日期时间")
	print ("check_phone				=>		校验是否手机号")
	print ("check_tel				=>		校验是否固定电话")
	print ("format_utf8				=>		将字符串强制转为utf-8")
	print ("format_gbk				=>		将字符串强制转为gbk")
	print ("host_ip					=>		获取本机ip，以第一个有网关的网卡的ip地址为本机ip地址")
	print ("host_gateway				=>		获取本机ip，以第一个有网关的网卡的ip地址为本机网关地址")
	print ("b64Urldecode				=>		先base64加密，再用urlcode加密")
	print ("urlB64encode				=>		先urlcode解密，再用base64解密")
	print ("is_Chinese				=>		判断是否为中文")
	print ("is_zh_punctuation			=>		判断是否为中文符号")
	print ("is_en					=>		判断是否为英文")
	print ("is_en_punctuation			=>		判断是否为英文符号")
	print ("keyword_filter_str			=>		过滤特殊字符")
	print ("rtsqsput				=>		从配置文件读取httpsqs相关信息，返回拼接后的httpsqs地址")
	print ("rtsqsget				=>		从配置文件读取httpsqs相关信息，返回拼接后的shell")
	print ("format_int				=>		强制转化为int制")
	
"""
格式化配置文件的内容

@param		string		filepath		文件路径

@return		dict		dict_config		格式化后的文件内容字典

"""
def get_config(filepath):
	if(os.path.exists(filepath)):
		dict_config={}
		f = open(filepath)               			# 返回一个文件对象 
		line = f.readline()               			# 调用文件的 readline()方法 
		while line: 
			line=line.strip()						#清除空格
			arr=line.split('=')						#分割
			if arr[0]:
				dict_config[arr[0]]=arr[1]
			line = f.readline() 
		f.close()
		return dict_config

"""
计算ip地址的掩码

@param		str		ipstr	单个IP范围

@return		dict	dict_config

"""
def ip_mask(ipstr):
	dict_config={}
	if('/' in ipstr):
		ipstrs=ipstr.split('/')
		base=IPy.IP('255.255.255.255').int()
		ip=IPy.IP(ipstrs[0]).int()
		mask=pow(2,32-int(ipstrs[1]))-1
		smask=mask ^ base
		min=ip & smask
		max=ip | mask
	elif('-' in ipstr):
		ipstrs=ipstr.split('-')
		min=IPy.IP(ipstrs[0]).int()
		max=IPy.IP(ipstrs[1]).int()
	else:
		min=max=IPy.IP(ipstr).int()
	dict_config["min"]=min
	dict_config["max"]=max
	return dict_config

"""
校验ip地址

@param		str		address		ip地址

@return		str

"""
def check_ip(address):
	try:
		if IPy.IP(address).version() == 4:
			return address
		return ""
	except Exception as e:
		return ""

"""
校验mac地址

@param		str		mac		mac地址

@return		str

"""
def check_mac(mac):
    try:
        if re.match(r"^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$", mac):
            return mac
        return ""
    except Exception as e:
        return ""

"""
校验多个mac地址

@param		str		macstrs		多个mac地址

@return		str

"""
def check_macs(macstrs):
	new_macstrs=""
	if(',' in macstrs):
		mac_arr=macstrs.split(',')
		for macsts in mac_arr:
			if check_mac(macsts)!="" and check_mac(macsts)!=None:
				new_macstrs=new_macstrs+str(check_mac(macsts))+","
		new_macstrs=new_macstrs.rstrip(',')
	elif(';' in macstrs):
		mac_arr=macstrs.split(';')
		for macsts in mac_arr:
			if check_mac(macsts)!="" and check_mac(macsts)!=None:
				new_macstrs=new_macstrs+str(check_mac(macsts))+";"
		new_macstrs=new_macstrs.rstrip(';')
	else:
		new_macstrs=check_mac(macstrs)
	return new_macstrs

"""
校验单个ip范围

@param		str		iprange		单个IP范围

@return		str

"""
def check_iprange(iprange):
	try:
		if('/' in iprange):
			ipstrs=iprange.split('/')
			if int(ipstrs[1]) in range(0,32):
				if check_ip(ipstrs[0])!="" and check_ip(ipstrs[0])!=None:
					return iprange
		elif('-' in iprange):
			ipstrs=iprange.split('-')
			if check_ip(ipstrs[0])!="" and check_ip(ipstrs[0])!=None and check_ip(ipstrs[1])!="" and check_ip(ipstrs[1])!=None:
				return iprange
		else:
			return check_ip(iprange)
	except Exception as e:
		return ""

"""
校验多个ip范围

@param		str		iprange		ip范围

@return		str

"""
def check_ipranges(iprange):
	new_ipstrs=""
	if(',' in iprange):
		ipstrs=iprange.split(',')
		for ipstr in ipstrs:
			if check_iprange(ipstr)!="" and check_iprange(ipstr)!=None:
				new_ipstrs=new_ipstrs+str(check_iprange(ipstr))+","
		new_ipstrs=new_ipstrs.rstrip(',')
	elif(';' in iprange):
		ipstrs=iprange.split(';')
		for ipstr in ipstrs:
			if check_iprange(ipstr)!="" and check_iprange(ipstr)!=None:
				new_ipstrs=new_ipstrs+check_iprange(ipstr)+";"
		new_ipstrs=new_ipstrs.rstrip(';')
	else:
		new_ipstrs=check_iprange(iprange)
	return new_ipstrs

"""
校验邮箱格式

@param		str		email	邮箱

@return		str

"""
def check_email(email):
	try:
		if re.match(r"^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+", email):
			return email
		return ""
	except Exception as e:
		return ""

"""
校验是否整数

@param		str or int		number		整数

@return		str

"""
def check_int(number):
	try:
		if re.match(r"^[1-9]\d*$", str(number)):
			return str(number)
		return "0"
	except Exception as e:
		return "0"

"""
校验是否日期

@param		str		date	日期,格式是1970-01-01

@return		str

"""
def check_date1(date):
	try:
		if re.match(r"^[1-9]\d{3}-(0[1-9]|1[0-2]|[1-9])-(0[1-9]|[1-2][0-9]|3[0-1]|[1-9])$", str(date)):
			return str(date)
		return "0"
	except Exception as e:
		return "0"

"""
校验是否日期

@param		str		date	日期,格式是1970/01/01

@return		str

"""
def check_date2(date):
	try:
		if re.match(r"^[1-9]\d{3}/(0[1-9]|1[0-2]|[1-9])/(0[1-9]|[1-2][0-9]|3[0-1]|[1-9])$", str(date)):
			return str(date)
		return "0"
	except Exception as e:
		return "0"

"""
校验是否日期时间

@param		str		date	日期时间,格式是1970-01-01 12:00:00

@return		str

"""
def check_datetime1(datetime):
	try:
		if re.match(r"^[1-9]\d{3}-(0[1-9]|1[0-2]|[1-9])-(0[1-9]|[1-2][0-9]|3[0-1]|[1-9])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$", str(datetime)):
			return str(datetime)
		return "0"
	except Exception as e:
		return "0"

"""
校验是否日期时间

@param		str		date	日期时间,格式是1970/01/01 12:00:00

@return		str

"""
def check_datetime2(datetime):
	try:
		if re.match(r"^[1-9]\d{3}/(0[1-9]|1[0-2]|[1-9])/(0[1-9]|[1-2][0-9]|3[0-1]|[1-9])\s+(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$", str(datetime)):
			return str(datetime)
		return "0"
	except Exception as e:
		return "0"

"""
校验是否日期时间

@param		str		date	日期时间,格式是1970-01-01 12:00

@return		str

"""
def check_datetime3(datetime):
	try:
		if re.match(r"^[1-9]\d{3}-(0[1-9]|1[0-2]|[1-9])-(0[1-9]|[1-2][0-9]|3[0-1]|[1-9])\s+(20|21|22|23|[0-1]\d):[0-5]\d$", str(datetime)):
			return str(datetime)
		return "0"
	except Exception as e:
		return "0"

"""
校验是否日期时间

@param		str		date	日期时间,格式是1970/01/01 12:00

@return		str

"""
def check_datetime4(datetime):
	try:
		if re.match(r"^[1-9]\d{3}/(0[1-9]|1[0-2]|[1-9])/(0[1-9]|[1-2][0-9]|3[0-1]|[1-9])\s+(20|21|22|23|[0-1]\d):[0-5]\d$", str(datetime)):
			return str(datetime)
		return "0"
	except Exception as e:
		return "0"

"""
校验是否手机号

@param		str		text	手机号

@return		str

"""
def check_phone(text):
	try:
		if re.match(r"^[1][3,4,5,7,8][0-9]{9}$", str(text)):
			return str(text)
		return ""
	except Exception as e:
		return ""

"""
校验是否固定电话

@param		str		text	固定电话

@return		str

"""
def check_tel(text):
	try:
		if re.match(r"^\d{3}-\d{8}|\d{4}-\d{7,8}$", str(text)):
			return str(text)
		return ""
	except:
		return ""

"""
将字符串强制转为utf-8

@param		str		target		目标字符串

@return		str

"""
def format_utf8(target):
	try:
		target=target.decode("gbk").encode("utf-8")
	except:
		target=target
	return target
	
"""
将字符串强制转为gbk

@param		str		target		目标字符串

@return		str

"""
def format_gbk(target):
	try:
		target=target.decode("utf-8").encode("gbk")
	except:
		target=target
	return target
	
"""
获取本机ip，以第一个有网关的网卡的ip地址为本机ip地址

@param	NULL

@return	str

"""
def host_ip():
	eth_path = '/etc/sysconfig/network-scripts/'
	eth_arr = (os.popen('cd /etc/sysconfig/network-scripts/; ls | grep ifcfg | grep -v "ifcfg-lo"')).readlines()
	for eth in eth_arr:
		eth = eth.strip()
		eth_txt_list = (os.popen('cat ' + eth_path + eth)).readlines()
		ipaddr = ''
		gateway = ''
		for eth_txt in eth_txt_list:
			eth_txt = eth_txt.strip()
			if re.match('IPADDR', eth_txt):
				ipaddr = (eth_txt.split('='))[1]
			if re.match('GATEWAY', eth_txt):
				gateway =(eth_txt.split('='))[1]
			if ipaddr and gateway:
				return ipaddr

"""
获取本机ip，以第一个有网关的网卡的ip地址为本机网关地址

@param	NULL

@return	str

"""
def host_gateway():
	eth_path = '/etc/sysconfig/network-scripts/'
	eth_arr = (os.popen('cd /etc/sysconfig/network-scripts/; ls | grep ifcfg | grep -v "ifcfg-lo"')).readlines()
	gateway = ''
	for eth in eth_arr:
		eth = eth.strip()
		eth_txt_list = (os.popen('cat ' + eth_path + eth)).readlines()
		gateway = ''
		for eth_txt in eth_txt_list:
			eth_txt = eth_txt.strip()
			if re.match('GATEWAY', eth_txt):
				gateway =(eth_txt.split('='))[1]
			if gateway:
				return gateway


"""
先base64加密，再用urlcode加密

@param		str		text	待加密字符串

@return		str

"""
def	b64Urldecode(text):
	text = text.encode(encoding="utf-8")
	return urllib.parse.quote(base64.b64encode(text).decode())

"""
先urlcode解密，再用base64解密

@param		str		text	待加密字符串

@return		str

"""
def urlB64encode(text):
	text = text.encode(encoding="utf-8")
	return base64.b64decode(urllib.parse.unquote(text)).decode()

"""
判断是否为中文

@param  	string  w    字符串

@return     bool    True:是,False:不是

"""
def is_Chinese(w):
	try:
		if re.match(r"^.*[\u3002\uff1f\uff01\uff0c\u3001\uff1b\uff1a\u201c\u201d\u2018\u2019\uff08\uff09\u300a\u300b\u3008\u3009\u3010\u3011\u300e\u300f\u300c\u300d\ufe43\ufe44\u3014\u3015\u2026\u2014\uff5e\ufe4f\uffe5]+.*$", str(w)):
			return True
		if re.match(r"^.*[\u3220-\uFA29]+.*$", str(w)):
			return True
		return False
	except Exception as e:
		return False

"""
判断是否为中文符号

@param  string  word    字符串

@return     bool    True:是,False:不是   

"""
def is_zh_punctuation(w):
	punctuation_str = punctuation   #中文符号
	if w in punctuation_str:
		return True

	return False

"""
判断是否为英文

@param  string  word    字符串

@return     bool    True:是,False:不是   

"""
def is_en(w):
	if 'a'<=w<='z' or 'A'<=w<='Z':
		return True

	return False

"""
判断是否为英文符号

@param  string  word    字符串

@return     bool    True:是,False:不是   

"""
def is_en_punctuation(w):
	punctuation_string = string.punctuation
	if w in string.punctuation:
		return True

	return False

"""
过滤特殊字符

@param		str			w				待过滤的字符串
@param		list		word_list		不用的过滤的特殊字符

@return		str

"""
def keyword_filter_str(w, word_list = []):
	if w is not None and w != "":
		black_list = [';','\'','"','|','&','&&','||','`',':','@','*','+','/','%2F']
		key_list = ['UNION','AND','OR','LIKE','ONERROR','ONMOUSEOVER','ONCLICK','DOCUMENT.INNERHTML','DOCUMENT.WRITER(','WINDOW.LOCATION.HREF','$.HTML(']

		if isinstance(word_list, list) and len(word_list) > 0:
			black_list = list(set(black_list).difference(set(word_list)))
			key_list = list(set(key_list).difference(set(word_list)))

		#包含
		for item in black_list:
			w = w.replace(item, '')

		for item in black_list:
			if str.upper(str(w)) == str.upper(item):
				w = ''

	return w

"""
从配置文件读取httpsqs相关信息，返回拼接后的httpsqs地址

@param		str		name	获取表名

@return		str

"""
def rtsqsput(name):
	httpsqs_dict = get_config("/var/www/html/cloudmap_taihang/configFile/httpsqs.cfg")
	return httpsqs_dict['protocol'] + "://" + httpsqs_dict['ip'] + ":" + httpsqs_dict['port'] + "/?name=" + str(name) + "&opt=put&auth=" + httpsqs_dict['auth']


"""
从配置文件读取httpsqs相关信息，返回拼接后的shell

@param		str		name	获取表名

@return		str

"""
def rtsqsget(name):
	httpsqs_dict = get_config("/var/www/html/cloudmap_taihang/configFile/httpsqs.cfg")
	address = httpsqs_dict['protocol'] + "://" + httpsqs_dict['ip'] + ":" + httpsqs_dict['port'] + "/?charset=" + httpsqs_dict['charset'] + "&name=" + str(name) + "&opt=get&auth=" + httpsqs_dict['auth']
	return (os.popen("curl '" + address + "'").readlines())[0]

"""
强制转化为int

@param		str or int		w	待格式化的参数

@return		int

"""
def format_int(w):
	try:
		w = int(w)
	except:
		w = 0
	return w

if __name__ == "__main__":
	__help__()