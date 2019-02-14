class Solution:
    def solve(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        rows = len(board)
        cols = len(board[0])
                
        
        for i in range(rows):
            for j in [0, cols - 1]:
                if board[i][j] == 'O':
                    self.bfs(board, i, j)
                    
        for i in [0, rows - 1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    self.bfs(board, i, j)
                    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] =='D':
                    board[i][j] = 'O'
                else:
                    pass
                
    def bfs(self, board, i, j):
        rows = len(board)
        cols = len(board[0])
        queue = collections.deque([(i,j)])
        while queue:
            row, col = queue.popleft()
            if row >=0 and row < rows and col >= 0 and col < cols:
                if board[row][col] == 'O':
                    board[row][col] = 'D'
                    queue.append((row + 1, col))
                    queue.append((row - 1, col))
                    queue.append((row, col + 1)) 
                    queue.append((row, col - 1))

'''
这是一道很典型的用bfs做起来比较简单的习题：

有几个要注意的事项：

1.一般来说可以通过修改当前矩阵里面的值而替代新创建的visited数组
2.queue append时注意它的条件

'''