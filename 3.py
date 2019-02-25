# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用递归的思想进行合并
class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        # 判断当前节点是否为空, 做题时记得考虑特殊情况
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        # 记得在使用mergeTrees的时候, 需要在前面加self. 因为当前调用的函数是递归的
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
