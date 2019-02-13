vsclass Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        start = 1
        end = x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        
        if start * start < x:
            return start
        
        
        