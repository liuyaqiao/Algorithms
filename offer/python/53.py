# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return 0
        
        left = 0
        right = len(data) - 1
        while left + 1 < right:
            mid = left + (right - left)/2
            if data[mid] >= k:
                right = mid                
            else:
                left = mid
        if data[left] == k:
            small = left
        if data[right] == k and data[left] != k:
            small = right
        if data[left] != k and data[right] != k:
            return 0
                
        left1 = 0
        right1 = len(data) - 1
        while left1 + 1 < right1:
            mid = left1 + (right1 - left1)/2
            if data[mid] > k:
                right1 = mid
            else:
                left1 = mid
        if data[right1] == k:
            large = right1
        if data[left1] == k and data[right1] != k:
            large = left1

            
        return large - small + 1