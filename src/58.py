class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                count += 1
            else:
                if count == 0:
                    continue
                else:
                    return count
        return count