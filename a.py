#!/usr/bin/python
# -*- coding: UTF-8 -*-


import urllib2
import re
from urlparse import urlparse
import codecs

sitename='http://www.163.com'
sitename_parsed=urlparse(sitename)

response=urllib2.urlopen(sitename)
temp=response.read()
temp=temp.decode('gb2312','ignore').encode('utf-8')

f=open(sitename_parsed.netloc+'.txt', 'w')
f.write(temp)


