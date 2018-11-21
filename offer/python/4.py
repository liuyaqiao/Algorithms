# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i, j = len(array) - 1, 0
        if len(array) == 0:
            return False

        while i >= 0 and j < len(array[0]):
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                i -= 1
            else:
                j += 1
        return False