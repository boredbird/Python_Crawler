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

# Presto 查询
engine = create_engine('presto://bqbpm2.bqjr.cn:8080/hive/nbr')

print 'reading  ',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
df = pd.read_sql(sql=(r'select * from '+ 'nbr.phone_info_missing_20170810') , con=engine)
print 'done ',time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


#
# headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
#                'Accept - Encoding':'gzip, deflate',
#                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
#                'Connection':'Keep-Alive',
#                'Host':'www.ip138.com',
#                'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def get_phone_info(phone):
    url = requests.get('http://www.ip138.com:8080/search.asp?mobile=' + phone +'&action=mobile')
    url.encoding = 'gb2312'
    # wbdata = requests.get(url).text
    # 请求URL，获取其text文本
    wbdata = url.text
    soup = BeautifulSoup(wbdata, 'lxml')
    a = soup.select(".tdc2")
    print phone

    lc = len(a[1].contents) -1
    print a[1].contents[lc]
    province = a[1].contents[lc].split()[0]
    if len(a[1].contents[lc].split())>1:
        city = a[1].contents[lc].split()[1]
    else:
        city = province
    return province,city

class PhoneInfo(object):
    def __init__(self):
        self.phoneNum = ''
        self.province = ''
        self.city = ''

#
# rst = []
# phone = '13890171234'
# pinfo = PhoneInfo()
# pinfo.phoneNum = phone
# pinfo.province,pinfo.city = get_phone_info(phone)
# rst.append([pinfo.phoneNum.encode('utf-8'),pinfo.province.encode('utf-8'),pinfo.city.encode('utf-8')])


rst = []
for i in range(0,len(df)):
    phone = df['phone_num'][i]
    pinfo = PhoneInfo()
    pinfo.phoneNum = phone

    try:
        pinfo.province,pinfo.city = get_phone_info(phone)
    except Exception, e:
        continue

    rst.append([pinfo.phoneNum.encode('utf-8'),pinfo.province.encode('utf-8'),pinfo.city.encode('utf-8')])



df_append = pd.DataFrame(rst,columns=['phoneNum','province','city'])


# Presto 插入 太慢了
tablename = 'phone_info_missing_append'
print 'writing : ', tablename, ' ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
df_append.to_sql(tablename, con=engine, flavor=None, if_exists='append', index=False, chunksize=2000000)
print 'done ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))