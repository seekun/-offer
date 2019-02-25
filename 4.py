class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        result = []
        for i in range(num + 1):
            # range, 前闭后开, 要注意取值范围
            # 默认从0开始, 所以range(0, num + 1)可以写为range(num+1)
            binary = bin(i)
            count = 0
            for j in binary:
                if j == '1':
                    count = count + 1
            result.append(count)
            # 记得使用append来拓展list; 注意迭代器的使用, i, j, k
        return result

# class Solution:
#     def countBits(self, num):
#         res = []
#         for i in range(num+1):
#             count = 0
#             while i:
#                 i = i & (i - 1)
#                 print(i)
#                 count += 1
#             res.append(count)
#         return res


s = Solution()
print(s.countBits(5))
