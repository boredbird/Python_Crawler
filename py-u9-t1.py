#coding:utf-8
import requests
import re
import urllib
from urllib.request import urlopen
import chardet

table1=[]
url='http://u9service.ufida.com.cn/servicehome/kmindex.aspx'	
for i in range(110):
        paramsload = {'ver': '0', 'mmdul': '0','mdul': '0','qnum': '','qtitle': '','qcontent': '','page': str(i+1)}
        r = requests.get(url,params=paramsload)
        regex1=r'<td width="40">(.*?)</td>'
        pot1=re.compile(regex1)
        table_code1=re.findall(pot1,r.content.decode())
        table1.extend(table_code1)

file = open('test1.txt','w')
for j in table1:
    file.write(j+'\n')
file.close()



        
