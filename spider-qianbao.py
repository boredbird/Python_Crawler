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
url='http://www.qbao.com/ntask/adv/100963.html'
t={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0"
}

for i in range(1):
        r = requests.get(url,headers=t)
        regex1=r'<span id="taskReward">(.*?)</span>'#任务奖励（钱宝币）
        regex2=r'<em id="bqNum">(.*?)</em>'#宝券奖励
        regex3=r'<span id="taskMargins">(.*?)</span>'#保证金（钱宝币）
        regex4=r'<em id="totalDays">(.*?)</em>'#天
        regex5=r'<em id="taskPently">(.*?)</em>'#钱宝币
        regex6=r'<em id="taskStock">(.*?)</em>'#次
        pot1=re.compile(regex1)
        pot2=re.compile(regex2)
        pot3=re.compile(regex3)
        pot4=re.compile(regex4)
        pot5=re.compile(regex5)
        pot6=re.compile(regex6)
        table_code1=re.findall(pot1,r.content.decode('utf-8'))
        table_code2=re.findall(pot2,r.content.decode('unicode-escape'))
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
