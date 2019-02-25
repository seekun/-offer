# -*- coding:utf-8 -*-

# 使用双指针， 一个指针指向元素较小的数字， 一个指针指向元素较大的值。

# 如果有多对数字的和等于S，输出两个数的乘积最小的。
# 使用双指针的方式， 不需要考虑上面的附件条件。 
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        low = 0
        high = len(array) - 1
        # 套路： 使用指针来结束循环
        # small = 999999999999999999999999
        result = []
        while (low < high):
            cur = array[low] + array[high]
            if cur == tsum:
                # small = array[low] + array[high]
                result.append(array[low])
                result.append(array[high])
                return result
            elif cur > tsum:
                high -= 1
            else:
                low += 1
        return []
s = Solution()
print(s.FindNumbersWithSum([1,2,3,4], 7))