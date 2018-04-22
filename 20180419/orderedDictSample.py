# -*- coding: utf-8 -*-
from collections import OrderedDict

#FIFO先进先出的dict
class LastUpdatedOrderedDict(OrderedDict):
    
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containskey = 1 if key in self else 0
        if len(self) - containskey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containskey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

d = {'key1':1, 'key2': 2}
ldict = LastUpdatedOrderedDict(2)
ldict['key1'] = 'haha'
ldict['key1'] = 'hahanew'
ldict['key2'] = 'hahwnwna'
ldict['key3'] = 'hahasakjdga'
print(ldict)

# output:
# add: ('key1', 'haha')
# set: ('key1', 'hahanew')
# add: ('key2', 'hahwnwna')
# remove: ('key1', 'hahanew')
# add: ('key3', 'hahasakjdga')
# LastUpdatedOrderedDict([('key2', 'hahwnwna'), ('key3', 'hahasakjdga')])
