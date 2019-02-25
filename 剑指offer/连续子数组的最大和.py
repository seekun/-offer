# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array) <= 0:
            return 0
        # 比较两个值: 当前和 与 之前最大和
        nCurSum = 0
        nGreatestSum = array[0]
        for i in range(len(array)):
            # 如果当前和小于0, 把array[i]赋值给当前和, 抛弃之前为负的和, 从当前点, 开始计数
            if nCurSum <= 0:
                nCurSum = array[i]
            # 如果当前和大与0, 说明是可积累的, 所以进行累加
            else:
                nCurSum += array[i]
            # 当前和 与 之前最大和进行比较
            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum
        return nGreatestSum