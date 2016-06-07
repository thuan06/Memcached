#!/usr/bin/env python

import memcache

host = "localhost"
port = 11211
synchro = ".\n"
path = "/tmp/2016060601.txt"

str  = open(path,'r')
data = str.read().split(synchro)
data.pop()

mc = memcache.Client(['%s:%d' %(host,port)],debug=0)
for i in data:
	s=i.split(": ")
        mc.set(s[0],s[1])
        print s
