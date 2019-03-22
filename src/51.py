class Solution(object):
    def solveNQueens(self, n):
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
        
        self.dfs(visited, [], n, result)
        
        return result
    
    def dfs(self, visited, temp, n, result):
        if len(temp) == n:
            result.append(self.draw(temp))
     
        for i in range(n):
            if self.isValid(len(temp), visited, i) == False:
                continue
            visited['col'].add(i)
            visited['sum'].add(i + len(temp))
            visited['diff'].add(i - len(temp))
            self.dfs(visited, temp + [i], n, result)
            visited['col'].remove(i)
            visited['sum'].remove(i + len(temp))
            visited['diff'].remove(i - len(temp))
            
    def isValid(self, row, visited, col):
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if col - row in visited['diff']:
            return False
        return True
    
    def draw(self, temp):
        res = []
        for item in temp:
            part_str = ''
            for i in range(len(temp)):
                if i == item:
                    c = 'Q'
                else:
                    c = '.'
                part_str += c
            res.append(part_str)
        return res
        
    #draw的高级写法
    def draw(self, temp):
        board = []
        for i in range(len(temp)):
            col_str = ''.join(['Q' if temp[i] == c else '.' for c in range(len(temp))])
            board.append(col_str)
        return board
    
    
'''
每一次都从0-n中选择一个数，
选择n次，每次选择要满足nqueens的
条件，最后把取出的数画出来；
'''