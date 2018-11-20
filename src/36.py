class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        ##col
        for col in board:
            if self.col(col) == False:
                return False
        
        ##row
        for j in range(9):
            hashset = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in hashset:
                    return False
                else:
                    hashset.add(board[i][j])
        # return True
        
        
        ##3*3 sub
        #对于这样的九宫格，row是 i/3 * 3 + j/3
        #col 是 
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                if not self.col(block):
                    return False        
        return True
        
    def col(self, subList):
        hashtable = set()
        for i in subList:
            if i == '.':
                continue
            if i in hashtable:
                return False
            else:
                hashtable.add(i)
        return True
        