# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        # list 可以把字符串拆分成一个个的字符， 当做 list 的 item

        charList = list(ss)
        charList.sort()
        # 把字符串拆成字符，并进行排序
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            # 把大问题划分成子问题， i 作为分隔符， 一直在移动， 整个字符串的组合 = 首部到 i 的字符串组合 + （i+1）到尾部的字符串组合
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))
            for j in temp:
                pStr.append(charList[i] + j)
        return pStr

