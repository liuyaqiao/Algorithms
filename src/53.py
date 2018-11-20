class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        ##init
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        
        return max(dp)
        
        ##
        #state function
        #dp表示i之前subarray的最大和
        #dp[i] = max(dp[i - 1] + num[i], num[i])
        
        #dp [-2,1,-2,4,3,5,6,1,4]
        