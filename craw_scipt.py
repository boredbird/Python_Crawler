# -*- coding:utf-8 -*-
__author__ = 'maomaochong'
from urllib2 import urlopen

width = raw_input()
height = raw_input()

url = 'http://placekitten.com/' + width + '/' +height
kitten = urlopen(url).read()

f = open('D:/craw_down/kittens.jpeg','w')
f.write(kitten)
f.close()

