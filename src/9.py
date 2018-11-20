class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xStr = str(x)
        left = 0
        right = len(xStr) - 1
        while left < right:
            if xStr[left] != xStr[right]:
                return False
            left += 1
            right -= 1
        return True