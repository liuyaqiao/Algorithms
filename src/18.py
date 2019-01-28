class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums) < 4:
            return []
        
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target1st = target - nums[i]
            for j in range(i + 1, len(nums)):
                #去重#
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                target2nd = target1st - nums[j]
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    if nums[left] + nums[right] == target2nd:
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[left])
                        temp.append(nums[right])
                        res.append(temp)
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] < target2nd:
                        left += 1
                    else:
                        right -= 1
        return res
                
                
                