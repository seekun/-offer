# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        try:
            float(s)
            if s[0:2] != '-+' and s[0:2] != '+-':
                return True
            else:
                return False
        except:
            return False