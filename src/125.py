class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s = s.upper()
        start = 0
        end = len(s) - 1
        
        while start < end:
            if self.isAlp(s[start]) == False:
                start += 1
                continue
            if self.isAlp(s[end]) == False:
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
    
    def isAlp(self, ch):
        if ch >= '0' and ch <= '9':
            return True
        if ch >= 'a' and ch <= 'z':
            return True
        if ch >= 'A' and ch <= 'Z':
            return True
        return False