# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.head = None
        self.pre = None

    def Convert(self, pRootOfTree):
        self.inOrder(pRootOfTree)
        return self.head

    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        node.left = self.pre
        if self.pre != None:
            self.pre.right = node
        self.pre = node
        if self.head == None:
            self.head = node
        self.inOrder(node.right)
