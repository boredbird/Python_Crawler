# -*- coding:utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup

response = urllib2.urlopen("http://www.iwencai.com/stockpick/search?tid=stockpick&qs=sl_box_main_ths&w=南京港")
content=response.read()

'''
res = r'<div id="u_sp" class="s-isindex-wrap s-sp-menu"><a .*?>(.*?)</a></div>'
mm =  re.findall(
res, content, re.S|re.M)
for value in mm:
    print value
'''

soup = BeautifulSoup(content)
print soup.prettify()

