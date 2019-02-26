# 多数投票问题
# 使用 cnt 来统计一个元素出现的次数， 当遍历到的元素和统计元素相等时， cnt++， 否则 cnt--。
# 如果前面找了 i 个元素， 且 cnt==0， 说明前 i 个元素没有 majority，或者 majority 出现的次数少于i/2。 此时剩下的 n-i 个元素中， majority 的数目依然多于（n-i)/2

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        #
        majority = numbers[0]
        cnt = 0
        for i in numbers:
            if majority == i:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                majority = i
                cnt = 1
        cnt = numbers.count(majority)
        if cnt > len(numbers) / 2:
            return majority
        else:
            return 0

s = Solution()
print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))