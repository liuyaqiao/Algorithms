class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        if len(word) == 0:
            return True
        
        row = len(board)
        col = len(board[0])
        
        res = ''
        nums = 0
        for i in range(row):
            for j in range(col):
                if self.dfs(board, word, nums, i, j) == True:
                    return True
                
        return False
        
        
    def dfs(self, board, word, nums, i, j):
        if nums >= len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] == word[nums]:
            nums += 1
            c = board[i][j]
            board[i][j] = False
            res = self.dfs(board, word, nums, i + 1, j) or self.dfs(board, word, nums, i - 1, j) or self.dfs(board, word, nums, i, j + 1) or self.dfs(board, word, nums, i, j - 1)
            board[i][j] = c
            return res
         
     
'''
这是一道典型的深度有限搜素，也可以叫回溯法解决的问题：
回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。

在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根结点出发深度探索解空间树。当探索到某一结点时，要先判断该结点是否包含问题的解，
如果包含，就从该结点出发继续探索下去，如果该结点不包含问题的解，则逐层向其祖先结点回溯。（其实回溯法就是对隐式图的深度优先搜索算法）。

若用回溯法求问题的所有解时，要回溯到根，且根结点的所有可行的子树都要已被搜索遍才结束。
而若使用回溯法求任一个解时，只要搜索到问题的一个解就可以结束。

关键的几个要点是：
1.recursie call之后要退回之前的一个状态！！！
2.要注意递归函数的return type

来说一下dfs、回溯的区别：

如果在递归中，你需要从当前状态回到之前的状态，那么这步操作就是回溯，回溯是递归的时候一定会产生的很自然的操作，只不过大部分情况下不需要回溯。
回溯可以自己进行prune，不需要进行所有情况的枚举
'''
        
        