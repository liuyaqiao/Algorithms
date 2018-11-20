class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        top = 0
        left = 0
        right = len(matrix[0])
        bottom = len(matrix)
        
        i = 0
        result = []
        
        while left <= right and top <= bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1
            if top >= bottom:
                break
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1
            if left >= right:
                break
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1
            if top >= bottom:
                break
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if left >= right:
                break
        return result
##注意一下循环退出的条件