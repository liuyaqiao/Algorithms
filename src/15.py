class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ##corner case
        res = []
        if len(nums) < 3:
            return res
        
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = i + 1
            b = len(nums) - 1
            while a < b:
                if nums[a] + nums[b] == -nums[i]:
                    temp = []
                    temp.append(nums[i])
                    temp.append(nums[a])
                    temp.append(nums[b])
                    res.append(temp)
                    a += 1
                    b -= 1
                    while a < b and nums[a] == nums[a - 1]:
                        a += 1
                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1
                elif nums[a] + nums[b] > -nums[i]:
                    b -= 1
                else:
                    a += 1
        
        return res