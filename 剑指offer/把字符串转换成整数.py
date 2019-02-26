# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        ret = 0
        for i in range(len(s)):
            if (i == 0 and (s[i] == '+' or s[i] == '-')):
                continue
            if s[i] < '0' or s[i] > '9':
                return 0
            ret = ret * 10 + (s[i] - '0')
        if s[0] == '-':
            ret = 0 - ret
        return ret

s = Solution()
print(s.StrToInt('1234'))

# 未通过， 感觉此题考的可能性不大