# -*- coding:utf-8 -*-
# 二分查找, 即折半查找, 每次都能讲查找区间减半, 时间复杂度为O(logN)



# front 指向相对来说较大的数字, rear 指向相对来说较小的数字
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        # 头, 尾, 两个指针.
        front = 0
        rear = len(rotateArray) - 1
        # 设首元素为最小值
        minVal = rotateArray[0]
        # 初始时: front > rear
        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        else:
            # 头 与 尾 汇合时 停止
            while(rear - front) > 1:
                # 中间指针
                mid = (rear + front) // 2

                # 保持, front指向大数, rear指向小数
                if rotateArray[mid] > rotateArray[rear]:
                    front = mid
                elif rotateArray[mid] < rotateArray[front]:
                    rear = mid
                # 如果三个指针指向的数字都相同, 那么使用普通循环的方式, 得到最小数
                elif rotateArray[mid] == rotateArray[front] and rotateArray[front] == rotateArray[rear]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal


