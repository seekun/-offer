class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    # 递归解决问题
    def Mirror(self, root):
        # 如果树为空, 直接返回
        if root == None:
            return
        # 如果为叶子节点, 直接返回, 不需要交换
        if root.left == None and root.right == None:
            return root
        # 否则交换左右节点
        root.right, root.left = root.left, root.right

        # 递归对子节点调用交换节点
        self.Mirror(root.left)
        self.Mirror(root.right)


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
S.Mirror(pNode1)
print(pNode1.right.left.val)
