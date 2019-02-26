# -*- coding:utf-8 -*-

# 使用一个栈来模拟操作, 把 push 序列的数字依次压入辅助栈， 每次压入后， 比较辅助栈的栈顶元素和 pop 序列的首元素是否相等 相等的话就 pop 序列的首元素和辅助栈的栈顶元素
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            # 模拟入栈
            stack.append(i)
            # 如果栈不为空， 模拟出栈
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        # 如果栈不为空， 返回 False
        if len(stack):
            return False
        else:
            return True

pushV = [1,2,3,4,5]
popV = [4,5,3,2,1]
popVF = [4,5,2,1,3]
s = Solution()
print(s.IsPopOrder(pushV, popV))
