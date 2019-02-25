# -*- coding:utf-8 -*-
# 迭代实现, 相比起递归来讲, 时间复杂度更低, 减少了重复计算
class Solution:
    def jumpFloor(self, number):
        if (number <= 2):
            return number
        # 有两种选择, 有多次选择
        pre2 = 1
        pre1 = 2
        # 需要求多种选择的数量
        result = 1
        for i in range(2, number):
            result = pre1 + pre2
            pre2 = pre1
            pre1 = result
        return result
