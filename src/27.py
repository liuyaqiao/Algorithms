class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        count = 0
        
        for i in range(len(nums)):
            ##[3,3,2,2]
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
        