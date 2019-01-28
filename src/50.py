class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ##奇偶正负
        # 二分法
        
        if n == 0 or x == 1:
            return 1
        
        if n == 1:
            return x
        
        if n < 0:
            return 1/(x * self.myPow(x, -(n + 1)))
        
        res = 1.0
        
        while n > 1:
            if n % 2 == 1:
                res *= x
            x = x * x
            n = n // 2

        res *= x
        return res 