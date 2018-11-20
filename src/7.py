class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            isNeg = True
            x = -x
        else:
            isNeg = False
        
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
            
        if x < - 2 **31 or x > 2**31 - 1:
            return 0
        
        if isNeg == 1:
            return -res
        return res
    
##math问题要考虑负数对10的余数和一个范围的问
