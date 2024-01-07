# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2024/1/2
Last Modified: 2024/1/2
Description: 
"""
from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None

    return title


url = "http://www.baidu.com"
title = get_title(url)

if title:
    print(title)
else:
    print("title could not be found.")