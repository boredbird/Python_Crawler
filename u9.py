#coding:utf-8
import requests
import re
import urllib
from urllib.request import urlopen
import chardet
import sys
print(sys.stdout.encoding)

def automatic_detect(url):
	content = urllib.request.urlopen(url).read()
	result=chardet.detect(content)
	encoding=result['encoding']
	return encoding


url='http://u9service.ufida.com.cn/servicehome/kmindex.aspx'
paramsload = {'ver': '0', 'mmdul': '0','mdul': '0','qnum': '','qtitle': '','qcontent': '','page': '1'}
r = requests.get(url,params=paramsload)
print(r.url,automatic_detect(url))
print(r.encoding)
print(r.content)



regex=r'<td width="40">(.*?)</td>'
pot=re.compile(regex)
table_code=re.findall(pot,content)

# print(content)

