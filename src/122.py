class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        sum = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                sum = sum + prices[i] - prices[i - 1]
        
        return sum
            