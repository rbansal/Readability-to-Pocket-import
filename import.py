#!/usr/bin/env python
# encoding: utf-8
"""
import.py
"""

import sys
import json
import urllib2

username = sys.argv[1]
password = sys.argv[2]
apikey = sys.argv[3]
jsonfile = sys.argv[4]

json_data = open(jsonfile)
data = json.load(json_data)

output = [x[u'article__url'] for x in data]

for y in output:
	url = 'https://readitlaterlist.com/v2/add?username=' + username + '&password='+ password + '&apikey=' + apikey + '&url=' + y
	response = urllib2.urlopen(url)
	
json_data.close()