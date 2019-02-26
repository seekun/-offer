# -*- coding:utf-8 -*-

# 可以看成一个排序问题， 比较 S1+S2和 S2+S1 的大小， 如果 S1+S2<S2+S1， 那么应该把 S1排在前面
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        # 返回空字符串
        # labmda 匿名函数， 代码比较简洁， labmda 是为了减少单行函数的定义而存在的
        # 前面为传入的参数， 后面的函数体
        lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        # cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
        # 通过指定的比较方法来进行排序
        # reverse = True 降序 ， reverse = False 升序（默认）。
        array = sorted(numbers, cmp=lmb)
        return ''.join(str(i) for i in array)
#     把字符串拼接起来
