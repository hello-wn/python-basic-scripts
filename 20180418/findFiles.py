# -*- coding: utf-8 -*-
import os
res = []
def findFiles(currentdir):
    for x in os.listdir(currentdir):
    # x is filename
        relatePath = os.path.join(currentdir, x)
#        print(relatePath, x)
        if os.path.isfile(relatePath) and 'key' in x:
            res.append(relatePath)
        elif os.path.isdir(relatePath):
        # find in child dirs
            findFiles(relatePath)

if __name__ == '__main__':
    findFiles('.')
    print(res)
