class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        result = [[1]]
        #temp[r][c] = temp[r - 1][c - 1] + temp[r][c - 1]
        
        prev = [1,1]
        result.append(prev)        
        for i in range(2, numRows):
            temp = [0 for j in range(i + 1)]
        
            if i == 0:
                temp[0] = 1
            else:
                temp[0] = 1
                temp[i] = 1
                
            for k in range(1, i):
                temp[k] = prev[k - 1] + prev[k]
            result.append(temp)
            
            prev = temp            
            
        return result
                
            