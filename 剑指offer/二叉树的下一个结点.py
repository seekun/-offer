# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# 情况一： 如果一个节点的右子树不为空， 那么该节点的下一个节点是右子树的最左节点
# 情况二： 否则， 向上找第一个左链接指向的树包含该节点的祖先节点
class Solution:
    def GetNext(self, pNode):
        # 判断此节点的右子树是否为空， 如果不为空， 该节点的下一个节点为右子树的最左节点
        if pNode.right != None:
            node = pNode.right
            while(node.left != None):
                node = node.left
            return node
        else:
            # 否则， 向上找第一个左链接指向的树包含该节点的祖先节点
            # pNode.next 指向的是父节点
            while(pNode.next != None):
                parent = pNode.next
                if parent.left == pNode:
                    return parent
                pNode = pNode.next
        return None
