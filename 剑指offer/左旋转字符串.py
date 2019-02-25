# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # 思路: 先翻转前半个字符串, 然后再翻转后半个字符串, 最后把两个字符串合并之后再翻转
        a = s[:n][::-1]
        b = s[n:][::-1]
        return (a+b)[::-1]

        # if len(s) == 0:
        #     return ""
        # l = n % len(s)
        # return s[l:]+s[:l]
    # 牛客网上的输出, 其实就是返回return, 牛客网的样例过少, 很多题可能即使通过了, 也有问题
    # 面试官看重的是什么, 他想要的答案是什么? 你说出他预期的答案才算回答正确, 投机取巧对于面试没有任何好处


s = Solution()
print(s.LeftRotateString('abcdefg', 2))