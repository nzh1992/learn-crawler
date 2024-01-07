# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2024/1/2
Last Modified: 2024/1/2
Description: 
"""
# 假设网页中没有某个标签，bs4获取这个标签时返回值就是None。
# 针对这种情况，在获取标签后需要检查一下标签是否存在。

from urllib.request import urlopen

from bs4 import BeautifulSoup


url = "http://www.baidu.com"
html = urlopen(url)

bs = BeautifulSoup(html.read(), "html.parser")

# 获取一个不存在的tag
tag = bs.not_exist_tag
print(type(tag))    # output: <class 'NoneType'>

# 为了程序的健壮性，获取标签后，应该先检查这个对象。
# 如果直接调用未获取到的标签，会引发AttributeError异常。'NoneType' object has no attribute 'xxx'。
# 所以加一句if判断
if tag:
    print("获取到了标签")
else:
    print("没有获取到标签")
