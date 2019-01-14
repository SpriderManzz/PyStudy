# coding=utf-8
import os
abspath = os.path.abspath('.')
file_path = abspath + '\pi_digits.txt'

with open(file_path) as f:
    lines = f.readlines()  # 返回的lines属性为list列表
pi_string = ''
for line in lines:
    pi_string = pi_string + line.strip()
print(pi_string)