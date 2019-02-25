# -*- coding:utf-8 -*-
class Solution:
    # 初始化两个空战, list即为栈
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # stack1 作为进栈口, stack2 作为出栈口
    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
