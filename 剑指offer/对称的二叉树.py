# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 疑问: 递归, 什么时候需要独立写一个函数来实习递归.
    def isSymmetrical(self, pRoot):
        return self.selfIsSymmetrical(pRoot, pRoot)

    def selfIsSymmetrical(self, pRoot1, pRoot2):
        # 两个子树进行比较
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        # 最后为什么要返回这个结果, 用递归实现都有哪些共同点
        return self.selfIsSymmetrical(pRoot1.left, pRoot2.right) and self.selfIsSymmetrical(pRoot1.right, pRoot2.left)