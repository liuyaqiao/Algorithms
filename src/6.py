class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        #corner case
        
        if numRows == 0:
            return s
        
        res = []

        for i in range(numRows):
            res.append([])
        
        i = 0
        
        while i < len(s):
            for j in range(numRows):
                if i < len(s):
                    res[j].append(s[i])
                    i += 1
            for j in range(numRows - 2, 0, -1):
                if i < len(s):
                    res[j].append(s[i])
                    i += 1
        new_res = []
        for i in res:
            new_res.extend(i)
            
        return ''.join(new_res)