class Solution:
    def Add(self, num1, num2):
        while num2:
            sum = num1 ^ num2
            # 在没有进位的情况下, 两数的和
            num2 = (num1 & num2) << 1
            # 进位
            # 循环停止的原因: carry最右边
            num1 = sum & 0xFFFFFFFF
        return num1


s = Solution()
print(s.Add(4, 2))
hu