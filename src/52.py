class Solution:
    count = 0
    def totalNQueens(self, n: int) -> int:
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 0:
            return []
        
        result = []
        visited = {
            'col' : set(),
            'sum' : set(),
            'diff' : set(),
        }
        
        self.dfs(visited, 0, n)
        
        return self.count
    
    def dfs(self, visited, k, n):
        if k == n:
            self.count += 1
            return
     
        for i in range(n):
            if self.isValid(k, visited, i) == False:
                continue
            visited['col'].add(i)
            visited['sum'].add(i + k)
            visited['diff'].add(i - k)
            self.dfs(visited, k + 1, n,)
            visited['col'].remove(i)
            visited['sum'].remove(i + k)
            visited['diff'].remove(i - k)
            
    def isValid(self, row, visited, col):
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if col - row in visited['diff']:
            return False
        return True

'''
只统计数量就可以

'''