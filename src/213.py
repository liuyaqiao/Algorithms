class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)

        ##choose 0 or choose last to pick up a max

        return max(self.robHelper(0, len(nums) - 2, nums), self.robHelper(1, len(nums) - 1, nums))

    def robHelper(self, left, right, nums):

        ##to calculate the max of left to right

        ##corner case

        ##init
        dp = [0 for i in range(0, len(nums))]

        for i in range(left, right + 1):
            dp[i] = nums[i]
            
            
        if left == 0:
            dp[1] = max(nums[0], nums[1])    
            
        for i in range(2, right + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(dp)
        ##equation
        #dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])



        # print(dp)

        
        
        