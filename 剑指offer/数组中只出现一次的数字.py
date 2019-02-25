
# -*- coding:utf-8 -*-
# 两个不相同的元素在位级上必定有一位不同， 将数组中所有元素异或得到的结果为不存在重复的两个元素异或的结果

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        diff = 0
        for i in array:
            diff ^= i
        # 将数组中所有元素进行异或
        diff &= -diff
        # 用此得出 diff 最右侧不为0的位。
        result = []
        num1 = 0
        num2 = 0
        for i in array:
            if i & diff == 0:
                num1 ^= i
            else:
                num2 ^= i
        result.append(num1)
        result.append(num2)
        return result