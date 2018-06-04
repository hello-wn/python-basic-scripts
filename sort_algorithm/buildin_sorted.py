# -*- coding: utf-8 -*-
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]


alist = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
blist = sorted(alist, key=by_name)
print(blist)
#[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

clist = sorted(alist, key=by_score, reverse=True)
print(clist)
#[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]
