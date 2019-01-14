# -*- coding: utf-8 -*-
import requests as r
rs = r.get("https://www.baidu.com/")
print (rs.status_code)