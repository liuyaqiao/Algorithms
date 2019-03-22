class Solution:
    maxArea = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == False:
                    self.bfs(grid, i, j, visited)
                    
        
        return self.maxArea
    
    def bfs(self, grid, i, j, visited):
        queue = collections.deque([(i,j)])
        area = 0
        while queue:
            row, col = queue.popleft()
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                if grid[row][col] == 1 and visited[row][col] == False:
                    visited[row][col] = True
                    area += 1
                    queue.append((row + 1, col))
                    queue.append((row - 1, col))
                    queue.append((row, col - 1))
                    queue.append((row, col + 1))
                    self.maxArea = max(self.maxArea, area)