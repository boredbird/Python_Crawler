# coding:utf-8

# 引入相关模块
import requests
from bs4 import BeautifulSoup
import sys
import requests
import MySQLdb
import time
reload(sys)
sys.setdefaultencoding('utf-8')
today = time.strftime("%Y-%m-%d")

conn = MySQLdb.connect(host='10.83.4.61', user='root', passwd='123456', db='crawler', port=3306, use_unicode=True, charset="utf8")
cur = conn.cursor()

def get_stock_price(stock_id):
    url = requests.get("https://gupiao.baidu.com/stock/" + stock_id + ".html?from=aladingpc")
    url.encoding = 'utf-8'

    # 请求URL，获取其text文本
    wbdata = url.text

    # 对获取到的文本进行解析
    soup = BeautifulSoup(wbdata, 'lxml')

    # 从解析文件中通过select选择器定位指定的元素，返回一个列表
    news_titles = soup.select(".line1 dl dt")
    news_value = soup.select(".line1 dl dd")

    for i in range(len(news_titles)):
        #print news_titles[i].get_text(), news_value[i].get_text()
        cur.execute("insert into crawler.stock_pd_price(stock_no,stock_index,index_value,date) values(%s,%s,%s,%s)",
                                (stock_id, news_titles[i].get_text(),news_value[i].get_text(), today))
        conn.commit()



if __name__ == '__main__':
    count = cur.execute('select stock_id from crawler.stock_list')
    print count
    result = cur.fetchmany(count)
    for i in range(count):
        try:
            print 'running ',i,result[i]
            get_stock_price(result[i][0])
        except:
            print 'error ',i,result[i]
            continue

    cur.close()
    conn.commit()
    conn.close()
