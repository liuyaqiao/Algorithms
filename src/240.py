class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        i = rows - 1
        j = 0
        
        while i >= 0 and j < cols:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

'''
这种类型的题需要找一个一边增一边减的位置
然后用两根指针的方法去做
'''