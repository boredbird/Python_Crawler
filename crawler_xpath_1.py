# -*- coding:utf-8 -*-
from lxml import etree  #导入xpath
html = "http://jikexueyuan.com/course/"
selector=etree.HTML(html, parser=None, base_url=None)

#  提取文本
context=selector.xpath('//*[@id="useful"]/li/text()')
for each in context:
    print each
#  结果显示：这是第一条信息
#  这是第二条信息
#  这是第三条信息




#  提取属性
link=selector.xpath('//*[@id="url"]/a/@href')
for each in link:
    print each
# 结果显示：http://jikexueyuan.com
# http://jikexueyuan.com/course/

#提取标题
# title=selector.xpath('//*[@id="url"]/a/@title')
# print title[0]
#结果显示：极客学院课程库