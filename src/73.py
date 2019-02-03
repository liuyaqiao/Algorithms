class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None
        firstCol = 0
        firstRow = 0
        row = len(matrix)
        col = len(matrix[0])
                
        for i in range(row):
            if matrix[i][0] == 0:
                firstCol = 1
                break
        
        for j in range(col):
            if matrix[0][j] == 0:
                firstRow = 1
                break
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0
                    
        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0
        
        if firstCol == 1:
            for i in range(row):
                matrix[i][0] = 0
        if firstRow == 1:
            for j in range(col):
                matrix[0][j] = 0
        

'''
这个题的要求是把出现0的行列的其他元素都设成0:
因为直接在扫描中改动会影响后面的结果，所以我们把
扫描的结果记录在第一行第一列；之后通过对第一行第
一列的扫描去改变数值；
需要注意的是，我们不能直接使用第一行第一列的值；
需要先对第一行第一列的有没有0值进行记录，用于最后
修改第一行第一列的值；
需要注意的是：
后面的循环多数是从1开始；这种对col和row使用比较多
的问题最好设一个row和col

'''