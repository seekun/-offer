# 平衡二叉树左右子树高度差不超过1
# 判断一棵树是否为平衡二叉树: 左右子树的深度差距最大为1

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 便于在不同函数之间传递参数, 可以直接用self来修改数值
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.getDepth(pRoot)
        # 注意调用方式, 以及参数传递. self不需要传递. 
        return self.flag

    def getDepth(self, pRoot):
        # 空树
        if pRoot == None:
            return 0
        left = self.getDepth(pRoot.left)
        right = self.getDepth(pRoot.right)


        # 判断是否符合平衡二叉树的要求
        if abs(left - right) > 1:
            self.flag = False
        # 树的深度为 1(当前节点) + 左右子树中最大的
        return 1 + max(left, right)
