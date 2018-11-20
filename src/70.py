class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0] * (n + 1)
        if n == 0:
            return result
        subset = []
        # nums = [1,2]
        return self.dfs(0, n, result)


    def dfs(self, i, n, result):
        if i > n:
            return 0
        if i == n:
            return 1
        if result[i] > 0:
            return result[i]
        
        result[i] = self.dfs(i + 1, n, result) + self.dfs(i + 2, n, result)
        return result[i]

