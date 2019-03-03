class Solution:
    # 直接利用Python的trick, 写一个简单的排列数组, 顺序不变
    def ReorderOddEven(self, array):
        left = [x for x in array if x & 1]
        right = [x for x in array if not x & 1]
        return left + right

S = Solution()
# print(S.reOrderArray3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# print(S.ReorderOddEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(S.ReorderOddEven([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))