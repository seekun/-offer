# -*- coding:utf-8 -*-

# 设置两个指针, 分别指向数字1和数字2，并设这两个指针为 small和 big， 对 small和 big 求和， 如果和大于目标值， 则从当前和中删除 small值， 并把 small 值加一，如果和小于目标值， 则把
# big 值加一， 再把 big 值加入和中。 如果等于目标值，就输出 small 和 big 的序列， 同时把 big 加一一并加入和中， 继续之前的操作
class Solution:
    def FindContinuousSequence(self, tsum):
        # 临近值监测
        if tsum < 3:
            return []
        # 初始化指针
        small = 1
        big = 2
        middle = (tsum + 1) // 2
        curSum = small + big
        output = []  # 用于存储输出的结果
        # 循环条件， 由于需要的时连续正数序列，所以最少为两个数连续，所以可以使用 middle 来限制循环次数
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big + 1)))
                # 把联系的序列存起来
            while curSum > tsum and small < middle:
                # 如果当前和比预期和大， small 右移
                curSum -= small
                small += 1
                if curSum == tsum:
                    output.append(list(range(small, big + 1)))
            # 否则 big 左移
            big += 1
            curSum += big
        return output
