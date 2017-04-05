#coding:utf-8

import re
import urllib
from urllib.request import urlopen
from urllib.request import urlopen

def get_content(url):
	"""doc."""
	#html=urllib.urlopen(url)

	html=urllib.request.urlopen(url)
	content=html.read()
	content = content.decode()
	html.close()
	return content


def get_images(info):
	"""doc.
	<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=9fecfebb5f82b2b7a79f39cc01accb0a/93d3d458ccbf6c81bea24a57ba3eb13532fa404c.jpg" width="364" height="363" size="18000">
	"""
	regex=r'class="BDE_Image" src="(.+?\.jpg)"'
	pot=re.compile(regex)
	images_code=re.findall(pot,info)

	i=0
	for image_url in images_code:
		print(image_url)
		urllib.request.urlretrieve(image_url,'%s.jpg' % i)
		i+=1


info=get_content('http://tieba.baidu.com/p/4074420609')

print(get_images(info))