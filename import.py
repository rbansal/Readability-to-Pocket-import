#!/usr/bin/env python
# encoding: utf-8
"""
import.py
"""

import sys
import json
import urllib
import urllib2

username = sys.argv[1]
password = sys.argv[2]
apikey = sys.argv[3]
jsonfile = sys.argv[4]

json_data = open(jsonfile)
data = json.load(json_data)
json_data.close()

url_data = [dict(url=x['article__url']) for x in data]

url_dict = dict(zip(xrange(len(url_data)), url_data))

dump = json.dumps(url_dict)

url_read = []
url_starred = []

for y in data:
	print('read:' + str(y['archive']))
	if y['archive']:
		url_read.append(dict(url=y['article__url']))
	print('starred:' + str(y['favorite']))
	if y['favorite']:
		url_starred.append(dict(url=y['article__url'],tags='starred'))

url_dict_read = dict(zip(xrange(len(url_read)), url_read))
url_dict_starred = dict(zip(xrange(len(url_starred)), url_starred))

dump_read = json.dumps(url_dict_read)
dump_starred = json.dumps(url_dict_starred)
print(dump_read)
	
url = 'https://readitlaterlist.com/v2/send'
values = {'username' : username, 'password' : password, 'apikey' : apikey, 'new' : dump, 'read' : dump_read, 'update_tags' : dump_starred}

variables = urllib.urlencode(values)
req = urllib2.Request(url, variables)
response = urllib2.urlopen(req)
print response.read()
	
