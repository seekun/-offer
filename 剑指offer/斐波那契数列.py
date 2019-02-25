# -*- coding:utf-8 -*-

# 斐波那契数列
# 从0开始， f（0) = 0 ， f（1）= 1， f（n）= f（n-1） + f（n-2）
# 如果利用递归求解， 会重复计算一些子问题。递归是将一个问题划分为多个子问题求解， 动态规划也是如此， 但是动态规划会把子问题的解缓存起来， 从而避免重复求解子问题
# 考虑到第 i 项只与第 i-1和第i-2项有关， 因此只需要存储前两项的值就能求解第 i 项。
# 由于待求解的 n 小于40， 因此可以将钱40项的结果先计算
class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                tempArray[i % 2] = tempArray[0] + tempArray[1]
                # 只需要存储 n-1与 n-2个元素即可
        return tempArray[n % 2]
