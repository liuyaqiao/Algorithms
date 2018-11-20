class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        R = len(matrix)
        C = len(matrix[0])

        
        if R == 0:
            return False
        
        i = R - 1
        j = 0
        
        while i >= 0 and j < C:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
        