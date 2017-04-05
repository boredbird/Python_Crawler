import urllib
import chardet
from urllib.request import urlopen


def automatic_detect(url):
	content = urllib.request.urlopen(url).read()
	result=chardet.detect(content)
	encoding=result['encoding']
	return encoding


urls =["http://www.iplaypython.com/",
	"http://www.baidu.com",
	"http://www.163.com"]

for url in urls:
	print(url,automatic_detect(url))