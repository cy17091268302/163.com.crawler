#!/usr/bin/python
# -*- coding: UTF-8 -*-


import urllib2
import re
from urlparse import urlparse
import codecs

sitename='http://comment.news.163.com/news3_bbs/AMH82HUS00014JB5.html'
sitename_parsed=urlparse(sitename)

response=urllib2.urlopen(sitename)
temp=response.read()
#temp=temp.decode('gbk','ignore').encode('utf-8')

f=open(sitename_parsed.netloc+'.txt', 'w')
f.write(temp)


