# -*- coding:utf-8 -*-
# 思路： 把值为i 的元素调整到第 i 个位置上进行求解
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if len(numbers) == 0:
            return False
        for i in numbers:
            if i < 0 or i > len(numbers) - 1:
                return False
        for i in range(len(numbers)):
            while i != numbers[i]:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    index = numbers[i]
                    numbers[i], numbers[index] = numbers[index], numbers[i]
                    # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]

        return False


s = Solution()
dupulication = [0]

print(s.duplicate([1, 2, 2, 3], dupulication))