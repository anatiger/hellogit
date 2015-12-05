#!/usr/bin/python
import urllib2
page = urllib2.urlopen("http://s2.ilmiri.com/account/cronChickenPrice");
result = page.read()
#$//open("./tmp/output.html","w").write(result) # write to output.html
