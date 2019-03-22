class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ##corner case
        if m == 0 or n == 0:
            return 0
        
        #init
        
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

            
        #state equation
        #dp[i][j] = 
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]


'''
下面是记忆化搜索
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 0 or n < 0:
            return 0
        state = [[0 for _ in range(n)] for _ in range(m)]
        self.dfs(m, n, state,0,0)
        return state[0][0]
    
    def dfs(self, m, n, state,i,j):
        if i == m - 1 and j == n - 1:
            state[i][j] = 1
            return 1
        if i == m - 1:
            state[i][j] = self.dfs(m,n,state,i,j+1)
            return state[i][j]
        if j == n - 1:
            state[i][j] = self.dfs(m,n,state,i+1, j)
            return state[i][j]
        
        if state[i][j] != 0:
            return state[i][j]
        
        state[i][j] = self.dfs(m,n,state, i+1, j) + self.dfs(m,n,state,i,j+1)
        return state[i][j]