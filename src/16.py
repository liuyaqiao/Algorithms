import sys

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ##corner case
        res = []
        if len(nums) < 3:
            return res
        
        nums.sort()
        minVal = sys.maxsize
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                diff = abs(temp - target)
                if diff < minVal:
                    minVal = diff
                    res = temp
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    return target
            
        return res