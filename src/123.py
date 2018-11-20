class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #corner case
        if len(prices) < 2:
            return 0
        
        #state
        length = len(prices)
        profit = [[0 for i in range(length)] for j in range(3)]
        
        #init

            
        for i in range(1, 3):
            maxDiff = -prices[0]
            for j in range(1, length):
                # maxVal = 0
                profit[i][j] = max(profit[i][j - 1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, profit[i - 1][j] - prices[j])
                             
                
        return profit[2][length - 1]
            
        