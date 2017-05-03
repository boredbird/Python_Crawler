#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sqlite3
import win32crypt
from bs4 import BeautifulSoup
import requests
import urllib
import re
import sys
import os
from urllib2 import urlopen
from urllib2 import Request
sys.path.append('D:/Program Files/Anaconda2/Lib/site-packages/')

SOUR_COOKIE_FILENAME = r'C:\Users\maomaochong\AppData\Local\Google\Chrome\User Data\Default\Cookies'
DIST_COOKIE_FILENAME = '.\python-chrome-cookies'


def get_chrome_cookies(url):
    subprocess.call(['copy', SOUR_COOKIE_FILENAME, DIST_COOKIE_FILENAME], shell=True)
    conn = sqlite3.connect(".\python-chrome-cookies")
    ret_dict = {}
    for row in conn.execute("SELECT host_key, name, path, value, encrypted_value FROM cookies"):
        # if row[0] not in url:
        if row[0] != url:
            continue
        print(row[0])
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    subprocess.call(['del', '.\python-chrome-cookies'], shell=True)
    return ret_dict


# DOMAIN_NAME = '.lxxlxx.com'
# get_url = r'http://zhs.lxxlxx.com/tags/Chinese/2'
# response = requests.get(get_url, cookies=get_chrome_cookies(DOMAIN_NAME))
# print(response.text)

def get_viedo_url_list(page_id):
    DOMAIN_NAME = 'zhs.lxxlxx.com'
    page_url = r'http://zhs.lxxlxx.com/tags/Chinese/'+str(page_id)
    headers = {'Cookie': ['='.join((i, j)) for i, j in get_chrome_cookies(DOMAIN_NAME).items()][0]}
    url = requests.get(page_url,headers)
    url.encoding = 'utf-8'
    # 请求URL，获取其text文本
    wbdata = url.text

    # 对获取到的文本进行解析
    soup = BeautifulSoup(wbdata, 'lxml')

    # 从解析文件中通过select选择器定位指定的元素，返回一个列表

    sub_page_name_list = soup.select(".thumb a u")
    sub_page_url_list = soup.select(".thumb a")



    # sub_page_url = 'http://zhs.lxxlxx.com'+sub_page_url_list[0]
    # sub_page_name = sub_page_name_list[0]


    def get_sub_page_viedo(sub_page_url):
        url = requests.get(sub_page_url,headers)
        url.encoding = 'utf-8'
        # 请求URL，获取其text文本
        wbdata = url.text

        # 对获取到的文本进行解析
        soup = BeautifulSoup(wbdata, 'lxml')

        # 从解析文件中通过select选择器定位指定的元素，返回一个列表

        sub_page = soup.select(".bigcolumn div script:nth-of-type(2)")
        sub_page_viedo_url = re.findall(r"video_url: (.+?),\r\n",sub_page[0].text)[0]

        sub_page_viedo_url = sub_page_viedo_url.encode('utf-8')
        print sub_page_viedo_url
        # local = os.path.join('D:/craw_down/1.mp4')

        # urllib.urlretrieve('http://b-2.lxxlxx.com:81/uuauth/move/201611/6048_6J8bo.mp4', local, Schedule)

        # urllib.urlretrieve(sub_page_viedo_url, "%s.mp4" % sub_page_name)

        # file = urllib2.urlopen(sub_page_viedo_url).read()
        # open(sub_page_name, "wb").write(file)


        # sub_page_viedo_url = 'http://b-2.lxxlxx.com:81/uuauth/move/201611/6048_6J8bo.mp4'
        # req = Request(sub_page_viedo_url, headers=headers)
        # kitten = urlopen(req).read()

        # kitten = urlopen(sub_page_viedo_url).read()
        #
        # f = open('D:/craw_down/'+ sub_page_name +'.mp4', 'w')
        # f.write(kitten)
        # f.close()



    #
    # import urllib2
    #
    # url = "http://b-2.lxxlxx.com:81/uuauth/move/201611/6048_6J8bo.mp4"
    #
    # local = os.path.join('D:/craw_down/','japans-next-teen-idol.mp4')
    #
    # urllib.urlretrieve(url,local,Schedule)

    #
    #
    # url = "http://s1-kk.bbbplayer.com/tw3623yukari-japans-next-teen-idol.mp4"
    # response = urllib2.urlopen(url)
    # print response.info()
    #
    # sub_page_viedo_url = 'http://s1-kk.bbbplayer.com/tw3623yukari-japans-next-teen-idol.mp4'
    # req = Request(sub_page_viedo_url, headers=headers)
    # kitten = urlopen(req).read()

    # kitten = urlopen(sub_page_viedo_url).read()
    #
    # f = open('D:/craw_down/' + sub_page_name + '.mp4', 'w')
    # f.write(kitten)
    # f.close()

    for i in range(len(sub_page_url_list)):
        sub_page_url_list[i] = sub_page_url_list[i]['href']
        # sub_page_name_list[i] = sub_page_name_list[i].encode("utf-8")
        get_sub_page_viedo('http://zhs.lxxlxx.com'+sub_page_url_list[i])




for page_id in range(2,17):
    get_viedo_url_list(page_id)