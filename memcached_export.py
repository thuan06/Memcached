#!/usr/bin/env python
import subprocess
import memcache

host1 = "43.239.220.132"
port1 = 11211
path = "/tmp/out.txt"

host2 = "43.239.220.133"
port2 = 11211

#--------------- Key export to file -------------
key = subprocess.call("memdump --servers=%s" %host1,stdout=open("%s"%path, 'w'),shell=True)
print "Kex Exported"
#--------------Save key:value to a dic ------------
m1 = memcache.Client(['%s:%d' %(host1,port1)],debug=0)

lines = [line.rstrip('\n') for line in open('%s'%path)]
print lines
mem={}
for i in lines:
        value=m1.get(i)
        mem[i]=value
#-----------Export dict to new server --------------
m2 = memcache.Client(['%s:%d' %(host2,port2)],debug=0)
for i in mem.keys():
        m2.set(i, mem.get(i))
