class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ##深度优先搜索
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                ans += 1
                self.dfs(grid, i, j)
        return ans
    
    def dfs(self, grid, i, j):
        
        row = len(grid)
        col = len(grid[0])
        
        if i < 0 or i >= row or j < 0 or j >= col: 
            return
        
        if grid[i][j] == '1':
            grid[i][j] = '0'
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)


###BFS


class Solution():
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if (grid == [] or grid == None):
            return 0
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if (visited[i][j] == False and grid[i][j] == '1'):
                    numIslands += 1
                    self.BFS(i, j, visited, grid)
        return numIslands
    
    def BFS(self, i, j, visited, grid):
        ##通过两个数组来控制方向，更新数据的时候只需要用一个for循环，但是不能用赋值语句，而要使用row + dx[i], 不能再循环中改变每一个row的值
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
    
        rows = len(grid)
        cols = len(grid[0])
        queue = [(i, j)]
        while (queue != []):
            row, col = queue.pop()
            if (row >= 0 and row < rows and col >= 0 and col < cols):
                if (visited[row][col] == False and grid[row][col] == '1'):
                    visited[row][col] = True
                    for j in range(4):
                        queue += [(row + dx[j], col+dy[j])]
    ##通过bfs和dfs都可以解决的问题，一般通过bfs更加简单和快捷。
        

class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        number = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]

                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == False:
                    number += 1
                    self.bfs(visited, grid, i, j)
        
        return number
        
    def bfs(self, visited, grid, i, j):
        queue = collections.deque([(i,j)])
        while queue:
            row, col = queue.popleft()
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                if visited[row][col] == False and grid[row][col] == '1':
                    visited[row][col] = True
                    queue.append((row + 1, col))
                    queue.append((row - 1, col))
                    queue.append((row, col - 1))
                    queue.append((row, col + 1))
                    
        


##还可以通过并查集的方法求解：
class Solution():   
    father = []
       
    def find(self, x):
        if x == self.father[x]:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
            
    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a != b:
            self.father[b] = a
    
    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        self.father = [i for i in range(rows * cols)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    if i > 0 and grid[i - 1][j] == '1':
                        self.union(i * cols + j, (i - 1) * cols + j)
                    if i < rows - 1 and grid[i + 1][j] == '1':
                        self.union(i * cols + j, (i + 1) * cols + j)
                    if j > 0 and grid[i][j - 1] == '1':
                        self.union(i * cols + j, i * cols + j - 1)
                    if j < cols - 1 and grid[i][j + 1] == '1':
                        self.union(i * cols + j, i * cols + j + 1)
                else:
                    k = i * cols + j
                    self.father[k] = -1
        count = 0
	#需要注意的是i的取值范围是rows - 1#
	#对k的i*cols+j的取值#
	#筛选的时候通过i和father[i]的值来判断#

        for i in range(cols * rows):
            if self.father[i] == i:
                count += 1
        return count
    

