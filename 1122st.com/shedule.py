# -*- coding:utf-8 -*-
__author__ = 'maomaochong'
#!/usr/bin/python

#encoding:utf-8

import urllib

import os

def Schedule(a,b,c):

    '''''

    a:已经下载的数据块

    b:数据块的大小

    c:远程文件的大小

   '''

    per = 100.0 * a * b / c

    if per > 100 :

        per = 100

    print '%.2f%%' % per,'已下载的大小:',a*b,'文件大小:',c

    #print '已经下载的数据块:',a#,'\n'

    #print '数据块的大小:',b#,'\n'

    #print '远程文件大小:',c,'\n'

    #print '已下载的大小:',a*b,'文件大小:',c

# url = 'https://docs.python.org/2/archives/python-2.7.10-docs-pdf-a4.zip'
sub_page_viedo_url = 'http://s1-kk.bbbplayer.com/tw3623yukari-japans-next-teen-idol.mp4'
#local = url.split('/')[-1]

# local = os.path.join('D:/craw_down/','Python-2.7.5.tar.bz2')
local = os.path.join('D:/craw_down/','japans-next-teen-idol.mp4')

urllib.urlretrieve(sub_page_viedo_url,local,Schedule)
