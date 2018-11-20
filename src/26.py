class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 0
        
        for i in range(1, len(nums)):
            if nums[count] != nums[i]:
                count += 1
                tmp = nums[count]
                nums[count] = nums[i]
                nums[i] = tmp
        
        
        return count + 1
        