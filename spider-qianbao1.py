#coding:utf-8
import re
import urllib
from urllib.request import urlopen

url='http://www.qbao.com/ntask/adv/100963.html'
html=urllib.request.urlopen(url)
content=html.read()
info = content.decode()
html.close()
regex=r'<span id="taskReward">(.*?)</span>'#任务奖励（钱宝币）
pot=re.compile(regex)
taskReward=re.findall(pot,info)

print(taskReward)
