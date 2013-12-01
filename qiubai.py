import urllib  
import urllib2
import sys
from BeautifulSoup import BeautifulSoup  

pages = int(sys.argv[1])
for i in range(1,pages+1):
	url = 'http://m.qiushibaike.com/hot/page/%d' % i
	req = urllib2.Request(url)  
	response = urllib2.urlopen(req)  
	soup = BeautifulSoup(response.read(),fromEncoding='utf-8')
	contents = soup.findAll('div',attrs={'class':'content'},title=True)
	for content in contents:
		print content.text+'\n'
