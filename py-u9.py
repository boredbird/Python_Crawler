#coding:utf-8
import requests
import re
import urllib
from urllib.request import urlopen
import chardet

table1=[]
table2=[]
table3=[]
table4=[]
table5=[]
table6=[]
url='http://u9service.ufida.com.cn/servicehome/kmindex.aspx'	
for i in range(110):
        paramsload = {'ver': '0', 'mmdul': '0','mdul': '0','qnum': '','qtitle': '','qcontent': '','page': str(i+1)}
        r = requests.get(url,params=paramsload)
        regex1=r'<td width="40">(.*?)</td>'
        regex2=r'<td width="140">(.*?)</a>'
        regex3=r'<td width="30">(.*?)</td>'
        regex4=r'问题现象：</font>(.*?)<br>'
        regex5=r'解决方案：</font>(.*?)</td>'
        regex6=r'<td width="70">(.*?)</td>'
        pot1=re.compile(regex1)
        pot2=re.compile(regex2)
        pot3=re.compile(regex3)
        pot4=re.compile(regex4)
        pot5=re.compile(regex5)
        pot6=re.compile(regex6)
        table_code1=re.findall(pot1,r.content.decode())
        table_code2=re.findall(pot2,r.content.decode())
        table_code3=re.findall(pot3,r.content.decode())
        table_code4=re.findall(pot4,r.content.decode())
        table_code5=re.findall(pot5,r.content.decode())
        table_code6=re.findall(pot6,r.content.decode())
        table1.extend(table_code1)
        table2.extend(table_code2)
        table3.extend(table_code3)
        table4.extend(table_code4)
        table5.extend(table_code5)
        table6.extend(table_code6)

    
file = open('test1.txt','w')
for j in table1:
    file.write(j+'\n')
file.close()

file = open('test2.txt','w')
for j in table2:
    file.write(j+'\n')
file.close()

file = open('test3.txt','w')
for j in table3:
    file.write(j+'\n')
file.close()

file = open('test4.txt','w')
for j in table4:
    file.write(j+'\n')
file.close()

file = open('test5.txt','w')
for j in table5:
    file.write(j+'\n')
file.close()

file = open('test6.txt','w')
for j in table6:
    file.write(j+'\n')
file.close()


        
