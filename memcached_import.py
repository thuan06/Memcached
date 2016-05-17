import memcache

host = "43.239.220.132"
port = 11211
path = "/root/test/out.txt"

lines = [line.rstrip('\n') for line in open('%s'%path)]
n=len(lines)
d=int(n/2)

mc = memcache.Client(['%s:%d' %(host,port)],debug=0)
if n>0:
        for i in range(d):
                mc.set("%s" %(lines[i]), "%s" %(lines[i+d]))
        print "Key imported"
else:
        print "No new key imported"


