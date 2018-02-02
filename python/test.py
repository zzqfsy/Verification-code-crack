#coding=utf-8
from PIL import Image,ImageFilter
img = Image.open(r'E:/code/github/python/Verification-code-crack\captchas\1.gif')  # 打开图片
img = img.convert('RGB')  # 转换为RGB图
pixdata = img.load()
img.show('pixdata')
img.show(pixdata)
