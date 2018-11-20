class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ##corner case
        if len(s) == 0:
            return ''

        
        ##init
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        #dp 表示从i到j这个subarray是不是回文
        # 要满足j - 1 >= i + 1
        #ababd
        #i j
        max_val = 0
        for j in range(len(s)):
            for i in range(j + 1):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                # print(j - i)
                if dp[i][j]:
                    if j - i + 1 > max_val:
                        max_val = j - i + 1
                        res = s[i:j + 1]
        # print(res)
        return res
                    