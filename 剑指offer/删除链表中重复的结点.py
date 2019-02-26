# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 使用递归； 子链表与链表问题的子问题。
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        next = pHead.next
        if pHead.val == next.val:
            # 有重复的节点， 需要删除
            while (next != None and pHead.val == next.val):
                next = next.next
                # 指向下一个节点， 即为删除节点
            return self.deleteDuplication(next)
        else:
            # 没有遇到重复节点， 指向下一个节点
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead