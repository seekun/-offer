# -*- coding:utf-8 -*-

# 引入一个队列来进行层序遍历
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        queue = []
        if not root:
            return []
        result = []
        queue.append(root)
        while len(queue) > 0:
            curRoot = queue.pop(0)
            result.append(curRoot.val)
            if curRoot.left:
                queue.append(curRoot.left)
            if curRoot.right:
                queue.append(curRoot.right)
        return result
