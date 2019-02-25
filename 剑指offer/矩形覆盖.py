# -*- coding:utf-8 -*-

# 思路：
# 第一个2*1的小矩阵有两种覆盖方法：一种是竖着放，此时总的覆盖方法等于剩下的n-1个2*1的大矩形的覆盖方法；另一种是横着放，此时需要另一个2*1的小矩形也必须横着放，此时总的覆盖方法等于剩下的n-2个2*1的大矩形的覆盖方法。总的方法f(n)=f(n-1)+f(n-2)。符合斐波那契数列


# 同斐波那契数列
class Solution:
    def rectCover(self, number):
        if (number <= 2):
            return number
        pre2 = 1
        pre1 = 2
        result = 0
        for i in range(3,number+1):
            result = pre2 + pre1
            pre2 = pre1
            pre1 = result
        return result