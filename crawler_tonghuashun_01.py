# coding:utf-8
import requests
import json
import time
import MySQLdb
import sys

conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='crawler', port=3306, use_unicode=True,
                       charset="utf8")
cur = conn.cursor()

def get_tech_vane(stock_no):
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    today = time.strftime("%Y-%m-%d")

    # 技术风向标
    url = 'http://www.iwencai.com/diag/block-detail?pid=8073&codes='\
          +stock_no+'&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A137%7D%7D%7D'
    wbdata = requests.get(url).text

    data = json.loads(wbdata)

    event = data['data']['data']['result']

    for key1,value1 in event.items():
        if isinstance(value1,dict):
            for key2, value2 in value1.items():
                for key3, value3 in value2.items():
                    if key3.encode('utf8') == 'query':
                        queryvalue = value3.encode("utf-8")
                        cur.execute("insert into crawler.stock_pd_tech_vane_test(stock_no,vane,date) values(%s,%s,%s)",
                                    (stock_no, queryvalue, today))


if __name__ == '__main__':
    count = cur.execute('select stock_no from crawler.stock_list')
    print count
    result = cur.fetchmany(count)
    for i in range(4245):
        try:
            get_tech_vane(result[i][0])
        except:
            print i,result[i]
            continue
    cur.close()
    conn.commit()
    conn.close()
