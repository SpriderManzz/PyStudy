import os
abspath = os.path.abspath('.')  # 查看当前目录的绝对路径
print(abspath)

img_path = os.path.join(abspath,'b')  # 在某个路径下创追加新的目录，
print(img_path)

img_path = os.mkdir(img_path) # 创建新的路径
print(img_path)
print(type(img_path))

#os.rmdir(img_path)   # 删除路径

