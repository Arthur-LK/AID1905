"""
regex1.py re模块 功能函数演示2
生成match对象的函数
"""

import re

s = "今年是2019年,建国70周年"
pattern = r'\d+'

# 返回迭代对象
it = re.finditer(pattern,s)

for i in it:
    print(i.group()) # 获取match对象对应内容

# 完全匹配一个字符串
m = re.fullmatch(r'[,\w]+',s)
print(m.group())

# 匹配开始位置
m = re.match(r'\w+?',s)
print(m.group())


# 匹配第一处符合正则规则的内容
m = re.search(r'\d+',s)
print(m.group())



