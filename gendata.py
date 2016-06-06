#!/usr/bin/env python

import memcache
import random
import string

host    = 'localhost'
port    = 11211
key_number = 10000

mc = memcache.Client(['%s:%s' %(host,port)],debug=0)

#Generate a string with upercase and digits
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

for i in range(key_number): #number of key/value
        key = 'key'+str(i)
        value=''
        value_len = random.randint(1,1000) #Lenght of value
        value = id_generator(value_len)
        mc.set(key,value)
        print key+'\t'+value+'\n'
print "Key generated!"
