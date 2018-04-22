# -*- coding: utf-8 -*-
import re
def is_valid_email(addr):
    re_email = re.compile(r'^[\w\.]*\@\w*\.\w*$')
    if re_email.match(addr):
        return True
    else:
        return False

# test:
assert is_valid_email('someone@gamil.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('OK')

def name_of_email(addr):
    m = re.match(r'.*?([\w\s]+).*', addr)
    if m:
        return m.group(1)
    else:
        return None

# test:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@hahah.org') == 'tom'
print('OK')
        

