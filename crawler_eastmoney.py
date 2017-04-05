# -*- coding:utf-8 -*-
from lxml import etree  #导入xpath
from bs4 import BeautifulSoup

html = "http://quote.eastmoney.com/stocklist.html"
selector=etree.HTML(html, parser=None, base_url=None)

# #  提取文本
# context=selector.xpath('/html/body/')
# print context

# for each in context:
#     print each

# soup = BeautifulSoup(html)
# print soup.div["quotebody"].div["sltit"].ul


soup = BeautifulSoup(open("stock.html"))
print(soup.prettify())