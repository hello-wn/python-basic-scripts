# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, uname, pwd):
        self.uname = uname
        self.salt = ''.join([chr(random.randint(20,80)) for i in range(15)])
        self.pwd = get_md5(pwd + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(uname, pwd):
    user = db[uname]
    return user.pwd == get_md5(pwd + user.salt)

# test:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('OK')
