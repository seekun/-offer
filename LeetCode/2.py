class Solution:
    def hammingDistance(self, x, y):
        # 计算两个数字对应二进制位不同位置的数目
        binary = x ^ y
        # ^ 为按位异或运算
        sbin = bin(binary)
        # bin() 转化为二进制
        final = 0
        for x in sbin:
            if x == '1':
                final += 1
        return final



s = Solution()
print(s.hammingDistance(1,32))