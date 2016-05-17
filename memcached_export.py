import subprocess

host = "43.239.220.132"
port = 11211
path = "/tmp/out.txt"

#---------------Save data-------------
key = subprocess.call("memdump --servers=%s" %host,stdout=open("%s"%path, 'w'),shell=True)
print "Kex Exported"
fo = open("%s" %path,"a")
value = subprocess.call("memcat --servers=%s `memdump --servers=%s`" %(host,host),stdout=open("%s"%path, 'a'), shell=True)
print "Value Exported"
fo.close()
