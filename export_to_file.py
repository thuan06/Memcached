#!/usr/bin/env python
import subprocess
import memcache

host1 = "localhost"
port1 = 11211
path = "/tmp/2016060601.txt" #yyyymmddns
synchro = ".\n"

#--------------- Key export to file -------------
key = subprocess.call("memdump --servers=%s" %host1,stdout=open("%s"%path, 'w'),shell=True)
print "Kex Exported"

#--------------Save key:value to a dic ------------
m1 = memcache.Client(['%s:%d' %(host1,port1)],debug=0)

#---------------Export key, value-------------
lines = [line.rstrip('\n') for line in open('%s'%path)]
print lines
mem={}
fi = open(path,'w')
for key in lines:
        value=m1.get(key)
        mem[key]=value
        fi.write(key+': '+value+synchro)
fi.close()
