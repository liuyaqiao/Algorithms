class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if  rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        result = [[1], [1,1]]
        prev = [1,1]
        
        for i in range(2, rowIndex + 1):
            temp = [0 for j in range(i + 1)]
            temp[0] = 1
            temp[i] = 1
            for j in range(1, i):
                temp[j] = prev[j - 1] + prev[j] 
            prev = temp
            
        return prev