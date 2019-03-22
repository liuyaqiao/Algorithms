class Solution:
    have = False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
    
        self.dfs(wordDict, s)
        return self.have
        
    def dfs(self, wordDict, s):
        if s == '':
            self.have = True
            return
        
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                self.dfs(wordDict, s[i:])
            else:
                continue
        

'''
用简单的dfs时间复杂度不通过；所以我们要使用带有mem的dfs；

'''
#2 dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        print(dp)            
        return dp[len(s)]

'''
这是dp的解法：
状态量dp表示第到字符串的第i的元素为止，能不能用字典里的词表示；
'''

#3 mem dfs

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # if not s or not wordDict:
        #     return False
        self.mem = {}
        return self.dfs(s, wordDict)
    
    def dfs(self, s, wordDict):
        if s in self.mem:
            return self.mem[s]
        if s in wordDict:
            self.mem[s] = True
            return True
        
        for i in range(1, len(s)):
            r = s[i:]
            if r in wordDict and self.dfs(s[0:i], wordDict):
                self.mem[s] = True
                return True
        self.mem[s] = False
        return False
        