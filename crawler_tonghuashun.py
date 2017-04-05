# coding:utf-8
import requests
import json
import time
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# url = 'http://www.toutiao.com/api/pc/focus/'
# wbdata = requests.get(url).text
#
# data = json.loads(wbdata)
# news = data['data']['pc_feed_focus']
#
# for n in news:
#   title = n['title']
#   img_url = n['image_url']
#   url = n['media_url']
#   print(url,title,img_url)

today = time.strftime("%Y-%m-%d")

# 技术风向标
url = 'http://www.iwencai.com/diag/block-detail?pid=8073&codes=000003&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A137%7D%7D%7D'
wbdata = requests.get(url).text

data = json.loads(wbdata)
# event = data['data']['data']['result']['event']
#
# for key1,value1 in event.items():
#     for key2, value2 in value1.items():
#         if key2.encode('utf8') == 'query':
#             print key2,value2


event = data['data']['data']['result']

conn = MySQLdb.connect(host='10.82.2.58', user='root', passwd='123456', db='crawler', port=3306, use_unicode=True, charset="utf8")
cur = conn.cursor()
# cur.execute('select * from crawler.stock_pd_tech_vane')

for key1,value1 in event.items():
    if isinstance(value1,dict):
        for key2, value2 in value1.items():
            for key3, value3 in value2.items():
                # print value3
                if key3.encode('utf8') == 'query':
                    queryvalue = value3.encode("utf-8")
                    print queryvalue
                    # cur.execute("insert into crawler.stock_pd_tech_vane_test(stock_no,vane,date) values(%s,%s,%s)",
                    #             ('000003', queryvalue, today))

cur.close()
conn.commit()
conn.close()

# cur.execute("insert into crawler.stock_pd_tech_vane(stock_no,vane,date) values(%s,%s,%s)"   % ('002040',queryvalue,today))
