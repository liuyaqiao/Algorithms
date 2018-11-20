class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        
        num = 0

        for i in range(len(haystack) - len(needle) + 1):
            if needle[0] == haystack[i]:
                for j in range(len(needle)):
                    if haystack[i + j] == needle[j]:
                        num += 1
                    else:
                        break
                if num == len(needle):
                    return i
                else:
                    num = 0
        
        return -1