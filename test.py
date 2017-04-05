import requests
import urllib
import chardet
from urllib.request import urlopen

import sysprint(sys.stdin.encoding)
print(sys.stdout.encoding)
'''
exp1 = re.compile("(?<a href="https://www.baidu.com/s?wd=isu&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1YLrH7bP1fYnHIbPAfkrjP90ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1D1rjcvrHfknjDYnWn3nH03nW0" target="_blank" class="baidu-highlight">isu</a>)<tr[^>]*>(.*?)</tr>")
exp2 = re.compile("(?<a href="https://www.baidu.com/s?wd=isu&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1YLrH7bP1fYnHIbPAfkrjP90ZwV5Hcvrjm3rH6sPfKWUMw85HfYnjn4nH6sgvPsT6K1TL0qnfK1TL0z5HD0IgF_5y9YIZ0lQzqlpA-bmyt8mh7GuZR8mvqVQL7dugPYpyq8Q1D1rjcvrHfknjDYnWn3nH03nW0" target="_blank" class="baidu-highlight">isu</a>)<td[^>]*>(.*?)</td>")
htmlSource = urllib.urlopen("<a href="http://cn-proxy.com/"" target="_blank">http://cn-proxy.com/"</a>).read()
for row in exp1.findall(htmlSource):
   print('===============')
   for col in exp2.findall(row):
       print col,
   print('===============')
 '''
 print('中文')