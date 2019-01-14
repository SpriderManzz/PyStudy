# coding =utf-8
import requests
import shelve

url = 'http://192.168.137.130/scm/login'
verifyCodeUrl = 'http://192.168.137.130/scm/login/validateCode'
s = shelve.sessions()

html = s.get(url).content
f = open('verifyCode.jpg', 'wb')
f.close()