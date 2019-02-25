# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # 使用两个栈, 一个为普通栈, 一个为最小栈
        self.stack = []
        self.minstack = []

    # 两个栈需要同时操作,
    def push(self, node):
        # write code here
        self.stack.append(node)
        # 其中"最小栈"中, 只能存最小值
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            temp = self.min()
            self.minstack.append(temp)

    def pop(self):
        # 记得考虑特殊情况, 如果stack或者minstack为空, 返回空
        if self.stack == [] or self.minstack == []:
            return None
        self.stack.pop()
        self.minstack.pop()
        # write code here

    # top: 读取栈顶元素
    def top(self):
        return self.stack[-1]
        # write code here

    # 读取最小栈中的元素, 记得要返回读取出的值, 自己敲的时候, 忘记返回值了
    def min(self):
        return self.minstack[-1]
        # write code here

# 注意: push和pop不需要返回return, 但是top和min需要返回值