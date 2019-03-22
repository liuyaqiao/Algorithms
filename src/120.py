class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        rows = len(triangle)
        cols = len(triangle[0])
        
        partSum = [[float('inf') for _ in range(rows)] for _ in range(rows)]
        self.dfs(partSum, 0, 0, triangle)
        return partSum[0][0]
        
        
    def dfs(self, partSum, i, j, triangle):
        if i == len(triangle):
            return 0
        
        if partSum[i][j] != float('inf'):
            return partSum[i][j]
        
        left = self.dfs(partSum, i + 1, j, triangle)
        right = self.dfs(partSum, i + 1, j + 1, triangle)
        
        partSum[i][j] = triangle[i][j] + min(left, right)
        
        return partSum[i][j]




'''
这个题简单的traverse和divide and conquer就不写了；
他们的时间复杂度过高；
这里写出的是带有记忆化搜索的dfs，和divide and conquer类似；
用一个数组来表示之前算出的结果；可以不需要再次计算；这样避免了重复计算；


'''