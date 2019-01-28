import sys
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #corner case
        if len(nums) == 0:
            return
        
        firstSmall = -1
        firstLarge = -1
        
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i] :
                firstSmall = i
                break
        if firstSmall == -1:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, firstSmall, -1):
                if nums[i] > nums[firstSmall]:
                    firstLarge = i
                    break
            nums[firstSmall], nums[firstLarge] = nums[firstLarge], nums[firstSmall]
        # print(firstSmall, firstLarge)
            self.reverseList(firstSmall + 1, len(nums) - 1, nums)
        
        
        
    def reverseList(self, i, j, nums):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
