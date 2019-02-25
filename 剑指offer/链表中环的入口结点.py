# # -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 设置两个快慢指针; 如果快慢指针相遇, 则快慢指针必然都在环中;
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 如果当前节点为空或者下一次节点为空, 返回None
        if pHead == None or pHead.next == None:
            return None
        slow = pHead.next, fast = pHead.next
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
        # 相当于其他语言中的do while
        # fast一次移动两个结点, slow一次移动一个节点, 当两个节点相遇时, 停止

        #   将fast重置到出发点, 重新开始移动, 这次fast和slow一起同时移动, 两个节点再次相遇的点, 就是环的入口
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def EntryNodeOfLoop(self, pHead):
#         # write code here
#         #遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
#         tempList = []
#         p = pHead
#         while p:
#             if p in tempList:
#                 return p
#             else:
#                 tempList.append(p)
#             p = p.next
