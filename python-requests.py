import requests
import urllib
import chardet
from urllib.request import urlopen
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")


def automatic_detect(url):
	content = urllib.request.urlopen(url).read()
	result=chardet.detect(content)
	encoding=result['encoding']
	return encoding


url='http://httpbin.org'
r = requests.get(url)

print(r.url)
print(url,automatic_detect(url))
print(r.encoding)
#print(r.content)
#r.encoding = 'ISO-8859-1'
#print(r.text)
print(r.raw)
