# 正则表达式

import re

str = '<div class="nam">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>', str)
# . 代表可有可无； * 代表任意字符；
# print(res)

a = [2, 1, 3]
a.sort()  # 从小到大排序
a.sort(reverse=True)  # 从大到小排序


s = ['a', 'd', 'j', 'l']
res = "".join(s)
# print(res) res = 'adjl'

a = 'not 404 张三 99 深圳'
list = a.split(" ")
# 用空格把字符串分割开
res = re.findall('\d+|[a-zA-Z]+',a)
# 用正则表达式匹配数字或者英文
for i in res:
    if i in list:
        list.remove(i)
        # 从 list 是移除某个元素， remove
new_str = " ".join(list)
# 使用空格把 list 中元素拼装成字符串
print(res)
print(new_str)