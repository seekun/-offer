# -*- coding:utf-8 -*-

# 使用一个栈来模拟操作, 把 push 序列的数字依次压入辅助栈， 每次压入后， 比较辅助栈的栈顶元素和 pop 序列的首元素是否相等 相等的话就 pop 序列的首元素和辅助栈的栈顶元素
class Solution:
    def IsPopOrder(self, pushV, popV):
