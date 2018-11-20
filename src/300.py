class Solution(object):
    def lengthOfLIS(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##corner case
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

    ##init

        dp = [1 for i in range(len(nums))]
    # dp[0] = 0

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    
        return max(dp)