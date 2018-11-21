# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        result = []
        if len(array) == 0:
            return result
        left = 0
        right = len(array) - 1
        while left < right:
            if array[left] + array[right] == tsum:
                result.append(array[left])
                result.append(array[right])
                left += 1
                right -= 1
                break
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                left += 1
        return result