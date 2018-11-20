class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        print(m,n)
        # if m == 0 or n == 0 :
#             return 0
        
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        print(dp)
        for i in range(1, m):
            print(obstacleGrid[i][0] != 0 and dp[i - 1][0] == 1)
            dp[i][0] = int(obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1)

                
        for j in range(1, n):
            dp[0][j] = int(obstacleGrid[0][j] == 0 and dp[0][j - 1] == 1)

        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
        print(dp)            
        return dp[m - 1][n - 1]
        # print(dp)