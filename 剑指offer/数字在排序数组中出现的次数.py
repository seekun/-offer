# -*- coding:utf-8 -*-

# 先用二分查找， 找到那个数字；
class Solution:
    def GetNumberOfK(self, data, k):
        # 一个查找 k， 一个查找 k + 1的位置， 由于是升序的，所以二者相减即可
        first = self.binarySearch(data, k)
        last = self.binarySearch(data, k + 1)
        # 排除特殊情况
        if first == len(data) or data[first] != k:
            return 0
        else:
            return last - first

    #
    def binarySearch(self, data, k):
        l = 0
        h = len(data)
        while (l < h):
            m = (l + h) // 2
            if data[m] >= k:
                h = m
            else:
                l = m + 1
        # 注意 m + 1
        return l


s = Solution()
print(s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 3))
