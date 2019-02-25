# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers == 0 or duplication.__len__() == 0:
            return False
        for i in range(numbers):
            while i != duplication[i]:
                if duplication[i] == duplication[duplication[i]]:
                    duplication[0] = i
                    return True
                tmp = duplication[i]
                duplication[i] = i
                i = tmp
        return False


s = Solution()
duplicaion = [2, 3, 1, 0, 2, 5, 3]
print(s.duplicate(7, duplicaion))
print(duplicaion)
