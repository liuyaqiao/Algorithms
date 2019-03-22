class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0
        state = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.dfs(state, 0, 0, grid)
        return state[0][0]

    def dfs(self, state, i, j, grid):
        # return miniumn sum with i, j
        if i == len(grid) - 1 and j == len(grid[0]) - 1 :
            state[i][j] = grid[i][j]
            return grid[i][j]
        if state[i][j] != float('inf'):
            return state[i][j]

        if i == len(grid) - 1:
            state[i][j] = self.dfs(state, i, j + 1, grid) + grid[i][j]
            return self.dfs(state, i, j + 1, grid) + grid[i][j]
        if j == len(grid[0]) - 1:
            state[i][j] = self.dfs(state, i + 1, j, grid) + grid[i][j]
            return self.dfs(state, i + 1, j, grid) + grid[i][j]

        state[i][j] = min(self.dfs(state, i + 1, j, grid), self.dfs(state, i, j + 1, grid)) + grid[i][j]
        return state[i][j]
'''
记忆化搜索：

关键点：

1. 这个思路相当于是自底向上，先递归到最下层，再一步一步向上
2. 这里的dfs一般是有返回值的，这个返回值和state矩阵中的值有关
3. 要注意更新边界点，和dp思路中的初始化一样，也要注意边界的初始化，也可以在开头进行初始化。

'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #先根据已知 可以得到[0,0], [1,0], [0,1]的大小，根据这个可以得到[1,1]的大小。之后
        #其实和普通的二维dp没有去区别，但是要考虑一个局部最优的问题，而且不需要考虑
        if len(grid) == 0:
            return 0
        
        #init
        dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid[0])):
            if i == 0:
                dp[0][i] = grid[0][0]
            else:
                dp[0][i] = grid[0][i] + dp[0][i - 1]
                
        for i in range(len(grid)):
            if i == 0:
                dp[i][0] = grid[0][0]
            else:
                dp[i][0] = grid[i][0] + dp[i - 1][0]
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                
        # print(dp)
            
        return dp[len(grid) - 1][len(grid[0]) - 1]

'''
dp解法比较常规和简单，是一个自顶向下的解法

'''