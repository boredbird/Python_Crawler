# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

import requests
from bs4 import BeautifulSoup

headers={
    "Host":"www.ip138.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive"
}

s=requests.session()
s.headers.update(headers)

html_url = s.get('http://www.ip138.com:8080/search.asp?mobile=18026940925&action=mobile',headers=headers)
print s.cookies.items()
print "html_url code %s" %html_url.status_code
html_txt = html_url.text

url = requests.get('http://www.ip138.com:8080/search.asp?mobile=18026940925&action=mobile')
url.encoding = 'gb2312'
# wbdata = requests.get(url).text
# 请求URL，获取其text文本
wbdata = url.text
soup = BeautifulSoup(wbdata, 'lxml')
a = soup.select(".tdc2")
print a[1].contents[1]
province = a[1].contents[1].split()[0]
city = a[1].contents[1].split()[1]

import re

string = "xxxxxxxxxxxxxxxxxxxxxxxx entry '某某内容' for aaaaaaaaaaaaaaaaaa"

result = re.findall(".*entry(.*)for.*", string)
for x in result:
    print x

result = re.findall(".*-->(.*)</td>",a[1])

for cont in soup.select(".tdc"):
    print cont.get_text().encode('utf-8')