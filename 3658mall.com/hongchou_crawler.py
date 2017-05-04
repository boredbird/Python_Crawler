#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import win32crypt
from bs4 import BeautifulSoup
import requests
import time
import sys
from sqlalchemy import create_engine
import pandas as pd
sys.path.append('D:/Program Files/Anaconda2/Lib/site-packages/')


page_url = r'https://www.3658mall.com/hongchou.html'
url = requests.get(page_url)
url.encoding = 'utf-8'
# 请求URL，获取其text文本
wbdata = url.text

# 对获取到的文本进行解析
soup = BeautifulSoup(wbdata, 'lxml')

# 从解析文件中通过select选择器定位指定的元素，返回一个列表

sub_page_url_list = soup.select(".chip_li div ul a")


def get_hongchou_sales(sub_page_url):
    url = requests.get(sub_page_url)
    url.encoding = 'utf-8'
    # 请求URL，获取其text文本
    wbdata = url.text

    # 对获取到的文本进行解析
    soup = BeautifulSoup(wbdata, 'lxml')

    # 从解析文件中通过select选择器定位指定的元素，返回一个列表

    hongchou_sales_index_list = soup.select(".item_sum p")
    print hongchou_sales_index_list[0].text
    print hongchou_sales_index_list[1].text

    cnt_1 = hongchou_sales_index_list[0].find_all('span')[0].string
    cnt_2 = hongchou_sales_index_list[1].find_all('span')[0].string
    return int(cnt_1),int(cnt_2)



def load_into_mysql(df,tablename):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    host = 'localhost'
    port = 3306
    db = 'dmr'
    user = 'root'
    password = '123456'

    engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s") % (user, password, host, db))

    try:
        print 'writing into mysql: ',tablename,' ',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        df.to_sql(tablename, con=engine, flavor=None, if_exists='append', index=False, chunksize=2000000)
        print 'done ',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    except Exception, e:
        print 'str(Exception):\t', str(Exception)
        print 'str(e):\t\t', str(e)
        print 'repr(e):\t', repr(e)
        print 'e.message:\t', e.message

    return  1


data = {}
hongchou_df = pd.DataFrame(data,columns=['page_id','idx_1','idx_2','craw_time'])
for link in sub_page_url_list:
    page_link = link.get('href')
    print(page_link)
    sub_page_url = 'https://www.3658mall.com/' + link.get('href')
    (cnt_1,cnt_2) = get_hongchou_sales(sub_page_url)

    data = {'page_id': [page_link],
            'idx_1': [cnt_1],
            'idx_2': [cnt_2],
            'craw_time': [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))],}

    df =pd.DataFrame(data,columns=['page_id','idx_1','idx_2','craw_time'])
    # df.to_csv('E:/3658mall/hongchou_sales.csv', index=False)
    hongchou_df = hongchou_df.append(df, ignore_index=True)
    time.sleep(1)


load_into_mysql(hongchou_df,'hongchou_sales')

