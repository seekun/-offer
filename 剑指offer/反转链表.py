# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 如果为空链表或者只有一个节点， 返回该节点； 同时也是递归的出口
        if pHead == None or pHead.next == None:
            return pHead
        next = pHead.next
        pHead.next = None
        newHead = self.ReverseList(next)
        next.next = pHead
        return newHead

        # 无法理解递归， 暂时放下

# CyC 笔记中有迭代的方法