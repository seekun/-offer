# -*- coding:utf-8 -*-
class Solution:

    def jumpFloorII(self, number):
        import math

        # dp = [0]*number
        # dp.append(1)
        # for i in range(1, number):
        #     for j in range(0,i):
        #         dp[i] = dp[i] + dp[j]
        # print(dp)
        # return dp[-1]

        return int(math.pow(2, number-1))

s = Solution()
print(s.jumpFloorII(2))