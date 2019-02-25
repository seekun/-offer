class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1/base

        result = self.Power(base, exponent >> 1)
        result *= result
        if (exponent & 0x1) == 1:
            result *= base
        return result

S = Solution()
print(S.Power(5, -10))