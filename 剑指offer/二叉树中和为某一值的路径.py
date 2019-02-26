# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归解决
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if root.left == None and root.right == None:
            if expectNumber == root.val:
                return [[root.val]]
            else:
                return []
        a = self.FindPath(root.left, expectNumber - root.val) + self.FindPath(root.right, expectNumber - root.val)
        return [[root.val] + i for i in a]
