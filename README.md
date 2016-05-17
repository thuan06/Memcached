Export data from memcached for backup or replication

Requirement:
- libmemcached
- python-memcached

Useage:
- memcached_export used to export data from memcached
    + host = ip running memcached
    + path = location save data
- memcached_import used to import data to memcached
    + path = path to data file
    + host = ip running memcached
