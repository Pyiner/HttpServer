#coding=utf-8
###
import requests

url = 'http://127.0.0.1:8000/imageup/'
path = u'D:\快盘\阿狸头像.jpg'
print path
files = {'file': open(path, 'rb')}


r = requests.put(url, files=files)
print r.url,r.text
