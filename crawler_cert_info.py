# coding:utf-8

# 引入相关模块
import requests
from bs4 import BeautifulSoup
import sys
import requests
import time
reload(sys)
sys.setdefaultencoding('utf-8')
today = time.strftime("%Y-%m-%d")

from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
import pandas as pd
import time


def get_cert_info(certId):
    url = requests.get('http://qq.ip138.com/idsearch/index.asp?action=idcard&userid=' + certId +'199203026934'+ '&B1=%B2%E9+%D1%AF')
    url.encoding = 'gb2312'
    # wbdata = requests.get(url).text
    # 请求URL，获取其text文本
    wbdata = url.text
    soup = BeautifulSoup(wbdata, 'lxml')
    a = soup.select(".tdc2")
    print a[2].contents[0]

    print certId
    str = a[2].contents[0].split()
    province = ''
    city = ''
    town = ''

    try:
        province = str[0]
        city = str[1]
        town = str[2]
    except Exception, e:
        pass

    return province,city,town

class CertInfo(object):
    def __init__(self):
        self.certId = ''
        self.province = ''
        self.city = ''
        self.town = ''


df = pd.read_csv('E:\\cert_seq6.csv')


rst = []
for i in range(0,len(df)):
    certId = df['cert_seq6'][i]
    cinfo = CertInfo()
    cinfo.certId = certId

    try:
        cinfo.province,cinfo.city,cinfo.town = get_cert_info(certId)
    except Exception, e:
        continue

    rst.append([cinfo.certId.encode('utf-8'),cinfo.province.encode('utf-8'),cinfo.city.encode('utf-8'),cinfo.town.encode('utf-8')])



df_append = pd.DataFrame(rst,columns=['cert_seq6','province','city','town'])

df_append.to_csv('E:\\cert_seq6_city_info.csv', index=False)

# Presto 插入 太慢了
engine = create_engine('presto://bqbpm2.bqjr.cn:8080/hive/nbr')
tablename = 'cert_seq6_city_info'
print 'writing : ', tablename, ' ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
df_append.to_sql(tablename, con=engine, flavor=None, if_exists='append', index=False, chunksize=2000000)
print 'done ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))