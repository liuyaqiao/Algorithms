class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        
        start = 1
        end = num
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                start = mid
            else:
                end = mid
        return False