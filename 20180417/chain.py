#-*- coding: utf-8 -*-
class Chain(object):

    def __init__(self, path=''):
        self._path = path
    
    def __call__(self, param):
        return Chain('%s/:%s' % (self._path, param))

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    
    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().users('Mike').repos(123))
