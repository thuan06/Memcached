Export data from memcached for backup or replication

Requirement:
- libmemcached
- python-memcached

Useage:
- memcached_export used to export data from memcached and export to new server
    + host1 = ip export memcached data
    + port1 = port running memcached on host1
    + path = path to save temp key file of host1
    + host2 = ip export memcached data
    + port2 = port running memcached on host2
