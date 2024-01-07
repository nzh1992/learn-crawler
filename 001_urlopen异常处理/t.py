# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2024/1/2
Last Modified: 2024/1/2
Description: 
"""
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


try:
    url = "http://www.baidu.com"
    html = urlopen(url)
except HTTPError as e:
    print(e)
    # 应对两种异常
    # 1. HTTP错误，包括404、500等
    # 2. 服务器不存在

    # 一般有两种处理
    # 1. 返回空值，中断程序
    # 2. 执行另一个方案
except URLError as e:
    print(e)
    # 服务器不存在，例如URL地址错误
else:
    # 获取成功
    print("ok.")

