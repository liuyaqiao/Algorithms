class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        prefix = ''
        
        for j in range(len(strs[0])):
            temp = strs[0][j]
            for i in range(len(strs)):
                if j >= len(strs[i]) or strs[i][j] != temp:
                    #注意or和and前后的条件顺序，会导致越界的事情
                    return prefix
                
            prefix += temp 
        return prefix