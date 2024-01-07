# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2024/1/7
Last Modified: 2024/1/7
Description: 
"""

# Lambda表达式
# 本质上就是一个函数，可以作为变量传入另一个函数


# 在BS中，find_all函数还可以接受lambda表达式作为查询条件。
# 注意：BS允许我们把特定类型的函数作为参数传入find_all函数，唯一的限制条件是，这些函数必须把一个标签对象
# 作为参数并且返回布尔类型的结果。通过此函数来评估BS遇到每个标签对象，评估结果为"真"则保留，否则剔除。

# 例如，获取有两个属性的所有标签
# bs.find_all(lambda tag: len(tag.attrs) == 2)