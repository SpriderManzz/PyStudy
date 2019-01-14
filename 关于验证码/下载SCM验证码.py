# coding=utf-8
import os
import time
import requests
from lxml import etree

# verifyCodeUrl = 'http://19v776387w.iask.in:12648/scm/login/validateCode'
verifyCodeUrl = 'http://192.168.137.130/scm/login/validateCode'

rs = requests.get(verifyCodeUrl)
img = etree.HTML(rs.content)  # img是页面对象

file_name = 'verifyCode_img'
verifyCode_name = time.strftime("%Y-%m-%d%H%M%S", time.localtime()) + '.png'

if not os.path.isdir(file_name):
    os.mkdir(file_name)
img_name = os.path.join(file_name, verifyCode_name)
file_path = os.path.abspath(img_name)
with open(file_path, 'wb') as f:
    f.write(rs.content)
    print (file_path+"下载成功")
