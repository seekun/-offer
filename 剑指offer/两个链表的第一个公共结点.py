# -*- coding:utf-8 -*-


# 设A的长度为 a + c, B的长度为 b + c, 其中c为尾部公共长度, 可知 a + c + b = b + c + a
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        I1 = pHead1
        I2 = pHead2
        while I1 != I2:
            if I1:
                I1 = I1.next
            else:
                I1 = pHead2
            if I2:
                I2 = I2.next
            else:
                I2 = pHead1
        return I1
