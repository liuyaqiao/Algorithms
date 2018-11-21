# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        start, end = 0, len(rotateArray) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if rotateArray[mid] <= rotateArray[end]:
                end = mid
            else:
                start = mid
        
        if rotateArray[start] > rotateArray[end]:
            return rotateArray[end]
        return rotateArray[start]