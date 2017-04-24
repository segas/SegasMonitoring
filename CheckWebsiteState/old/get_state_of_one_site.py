import urllib2
try:
	site = "http://www.meiertrans.ch/index.html"
	code = urllib2.urlopen(site).code
	print(code)
except urllib2.HTTPError as e:
	print(e.code)
