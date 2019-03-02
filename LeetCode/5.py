# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        # 计算树的最大深度, 使用递归的思想解决问题
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+ 1