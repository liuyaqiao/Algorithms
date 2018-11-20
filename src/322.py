import sys
##github

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        dp = [sys.maxsize for i in range(amount + 1)]
        dp[0] = 0
        for item in coins:
            if item <= amount:
                dp[item] = 1

        for i in range(1, amount + 1):
            for item in coins:
                if i >= item:
                    dp[i] = min(dp[i], dp[i - item] + 1)
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]


###
###这里cpp中 max_int + 1 = min_int  所以不能使用max_int 赋值
###
