# -*- coding:utf-8 -*-
__author__ = 'maomaochong'

# -*- encoding:utf8 -*-
import re
import sys
import urllib2
import urllib
import os


reload(sys)
sys.setdefaultencoding("utf-8")


def get_page(page_index):
    url = 'http://zhs.lxxlxx.com/tags/Chinese/' + str(page_index)
    html = urllib.urlopen(url).read()
    print html



if __name__ == '__main__':
    get_page(2)

"""
url_name = []
def get(pageindex):
    url = 'http://www.budejie.com/video/' + str(pageindex)
    # var1.set('已经获取到第%s页的视频视频'%(a))
    print url
    html = urllib.urlopen(url).read()
    url_reg = r'data-mp4="(.*?)"'
    url_items = re.findall(url_reg, html)
    name_reg = re.compile('<div class="j-r-list-c-desc".*?<a href=".*?>(.*?)</a>.*?</div>', re.S)
    name_items = re.findall(name_reg, html)
    for i, k in zip(name_items, url_items):
        url_name.append([i, k])

#传入文件名和video地址
def saveVideo(filename,videoUrl):
    print 'Saving : %s ...'%filename
    urllib.urlretrieve(videoUrl,'D:\\video\\%s.mp4'%filename)


####main exec ####
for pageindex in range(1,3):
    get(pageindex)

for index,item in enumerate(url_name):
    saveVideo(index,item[1])
"""