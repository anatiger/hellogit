#!/usr/bin/python
import urllib2
page = urllib2.urlopen("http://s2.ilmiri.com/invoice/cronMake")
result = page.read()
#/* Copyright (C) NAVER <http://www.navercorp.com> */
#$//open("./tmp/output.html","w").write(result) # write to output.html
