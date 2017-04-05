#-*-coding:utf-8-*-
import urllib
from urllib.request import urlopen

def callback(a,b,c):
	down_progress=100.0* a* b / c
	if down_progress>100:
		down_progress=100
	print("%.2f%%"%down_progress)

url ="http://www.iplaypython.com/"
local='D:\\python_pachong\\iplaypython.html'

urllib.request.urlretrieve(url,local,callback)
