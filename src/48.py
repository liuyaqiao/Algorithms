class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            for j in range(n/2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
            
                        
 '''
题目让我们对一个矩阵进行90度反转，遇到这种题我们要注意：

一般来说矩阵进行对角线反转或者某一个x、y方向的对称轴反转会比较方便，所以
考虑当前的操作能不能转换成这样的操作。

 '''       