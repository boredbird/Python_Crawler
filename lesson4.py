#-*-coding:utf-8-*-

# import urllib
# from urllib.request import urlopen

# url="http://blog.csdn.net/boredbird32"
# html=urllib.request.urlopen(url)

# print(html.read())

import urllib  
from urllib.request import urlopen
import urllib.request

url="http://blog.csdn.net/boredbird32"
req=urllib.request.Request(url,)

req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36")
req.add_header("GET",url)
req.add_header("Host","blog.csdn.net")
req.add_header("Referer","http://blog.csdn.net/")

html=urllib.request.urlopen(req)

print(html.read())