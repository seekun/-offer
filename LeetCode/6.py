# 位运算, ^ : 异或 , 相同为0 , 不同为1
# hashTable 哈希表, 散列表（Hash table，也叫哈希表），是根据键（Key）而直接访问在内存存储位置的数据结构。

# 解题代码 VS 解题思路
# 从解题代码, 回溯到解题思路, 难度很大. 反之会比较容易, 刷题的时候注意把握住解题思路





#  哈希表解法
class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        hash_table = {}
        # hash_table
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    # popitem()  , pop() 使用方法


# 位运算解法

s = Solution()
print(s.singleNumber([2, 2, 1]))
