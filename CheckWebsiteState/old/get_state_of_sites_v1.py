import urllib.error
from urllib.request import urlopen

text_file = open("sites.txt", "r")
lines = text_file.readlines()

for line in lines:
	line = line.rstrip('\n')
	try:
	        code = urlopen(line).getcode()
	        print(line , ": " , code)
	except urllib.error.HTTPError as e:
	        print(line , ": " , e.code)


text_file.close()
