class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n == 0:
            return []
        
        number = [i + 1 for i in range(n**2)]
        print(number)
        top = 0
        bottom = n
        left = 0
        right = n
        
        result = [[0 for i in range(n)] for i in range(n)]
        
        temp = 0
        
        while temp < n**2:
            print(temp)
            for i in range(left, right):
                result[top][i] = number[temp]
                temp += 1
            top += 1
            print(result)
            for i in range(top, bottom):
                result[i][right - 1] = number[temp]
                temp += 1
            right -= 1
            print(result)
            for i in range(right - 1, left - 1, -1):
                result[bottom - 1][i] = number[temp]
                temp += 1
            bottom -= 1
            print(result)
            for i in range(bottom - 1, top - 1, -1):
                result[i][left] = number[temp]
                temp += 1
            left += 1
            print(result)
            
        return result
            