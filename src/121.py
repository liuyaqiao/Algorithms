class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        if len(prices) == 1:
            return 0
        
        min = prices[0]
        maxDiff = prices[1] - min
        
        for i in range(2, len(prices)):
            if prices[i - 1] < min:
                min = prices[i - 1]
            currentDiff = prices[i] - min
            if currentDiff > maxDiff:
                maxDiff = currentDiff
                
        if maxDiff < 0:
            return 0
        return maxDiff