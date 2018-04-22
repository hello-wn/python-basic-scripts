#-*- coding: utf-8 -*-
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                a, b = b, a + b
                if x >= start:
                    L.append(a)
            return L
f = Fib()
print(f[0])
print(f[:10]) 
