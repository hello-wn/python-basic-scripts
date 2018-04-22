import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)



print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#communicate相当于键盘输入
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

# Same As:
# $ nslookup
# > set q=mx
# > python.org
# Server:     127.0.1.1
# Address:    127.0.1.1#53
# 
# Non-authoritative answer:
# python.org  mail exchanger = 50 mail.python.org.
# 
# Authoritative answers can be found from:
# > exit
