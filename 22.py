#coding:utf-8
import requests
import re
import urllib
from urllib.request import urlopen
import chardet

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
#print(r.content.decode())


regex=r'<td width="40">(.*?)</td>'
pot=re.compile(regex)
table_code=re.findall(pot,r.content.decode())

 print(table_code)

 file = open('test.txt','w')
 for i in table_code:
	file.write(i)
>>> file.close()
>>> table_code[1]

>>> for i in range(10):
	print(str(i+1))
	
url='http://u9service.ufida.com.cn/servicehome/kmindex.aspx'	
for i in range(110):
        paramsload = {'ver': '0', 'mmdul': '0','mdul': '0','qnum': '','qtitle': '','qcontent': '','page': +str(i+1)}
        r = requests.get(url,params=paramsload)
        regex=r'<td width="40">(.*?)</td>'
        pot=re.compile(regex)
        table_code=re.findall(pot,r.content.decode())
        file = open('test.txt','w')
        for j in table_code:
	file.write(i+'\n')
        file.close()
        

