class Solution:
    # 返回对应char
    def __init__(self):
        # 记得init中的self
        # 引入两个辅助存储空间. 一个Dict存储当前出现的字符以及字符出现的次数, 一个list存储当前出现字符
        # 维护一个队列
        self.adict = {}
        self.alist = []
    def FirstAppearingOnce(self):
        # 如果重复了的话, 就弹出, 弹出以及插入都是在alist中进行的
        while len(self.alist) > 0 and self.adict[self.alist[0]] == 2:
            self.alist.pop(0)
            # pop(0) 从前往后弹出;  pop()从后往前弹出
        if len(self.alist) == 0:
            return '#'
        else:
            return self.alist[0]

        # write code here
    def Insert(self, char):
        # 插入字符的时候, 判断该字符是否位于字典中
        if char not in self.adict.keys():
            self.adict[char] = 1
            self.alist.append(char)
        elif self.adict[char]:
            self.adict[char] = 2