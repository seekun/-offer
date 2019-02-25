# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # 如果A为空, 直接返回
        if A == None or len(A) <= 0:
            return
        length = len(A)
        # 初始化list
        aList = [1] * length

        for i in range(1, length):
            aList[i] = aList[i - 1] * A[i - 1]
        # print(aList)
        temp = 1
        for i in range(length - 2, -1, -1):
            # 从大到小, 逆序遍历
            temp = temp * A[i + 1]
            aList[i] *= temp
        return aList


test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))
