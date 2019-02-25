# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 层次遍历: 使用队列
# 先看答案, 别自己瞎写了, 这样只是在做无用功.

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # 用两个list, 一个用来装节点, 一个用来装节点的value
        A = []  # 用来装节点, 维护一个节点队列
        result = []  # 用来装节点的value
        if not pRoot:
            return result
        A.append(pRoot)
        # 入队列
        # 节点队列还有节点
        while A:
            tmp = [] # 存节点
            buf = [] # 存节点的值
            for i in A:
                buf.append(i.val)
                if i.left:
                    # 该节点入队列
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            result.append(buf)
            A = tmp
        return result

# class Solution:
#     # 返回二维列表[[1,2],[4,5]]
#     def __init__(self):
#         self.array = []
#         self.row = []
#
#     def Print(self, pRoot):
#         return self.array
#
#     def travel(self, pRoot):
#         if pRoot == None:
#             return
#         self.row.append(pRoot.val)
#         self.array.append(self.row)
#         if pRoot.left:
#             self.travel(pRoot.left)
#         if pRoot.right:
#             self.travel(pRoot.right)
