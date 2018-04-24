# -*- coding: utf-8 -*-
import requests

url = 'https://www.douban.com/'
#r = requests.get(url)
#print('code:', r.status_code)
#print('text: ', r.text)

#r_params = requests.get('https://www.douban.com/search', params = {'q': 'python', 'cat': '1001'})
#print('url:', r_params.url)
#print('code:', r_params.status_code)
#print(r_params.encoding)
#print(r.content)   #get bytes对象
#print(r_params.json())

#r_json = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
#print(r_json.json())

#r_headers = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
#print(r_headers.text[:500])

userData = {'form_email': 'test@email.com', 'form_pwd': '123456'}
r_post_json = requests.post('https://accounts.douban.com/login', data = userData)
#print(r_post_json.headers)
#print(r_post_json.cookies)

cs = {'token': '123421', 'status': 'working'}
r_cookies = requests.get(url, cookies=cs)

r_timeout = requests.get(url, timeout=2.5)
