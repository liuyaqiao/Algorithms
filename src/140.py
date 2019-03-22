class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return None
        result = []
        self.dfs(s, wordDict, '', result)
        return result
        
    def dfs(self, s, wordDict, temp, result):
        if s == '':
            result.append(temp[1:])
            return
        
        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                self.dfs(s[i:], wordDict, temp + ' ' + s[:i], result)
            else:
                continue

'''
dfs版本：时间复杂度太高，需要用记忆化搜索来储存中间结果；
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return None
        self.mem = {}
        return self.dfs(s, wordDict)
        
    def dfs(self, s, wordDict):
        # 当前字符串对应的所有解: ['','']
        if s in self.mem:
            return self.mem[s]
        
        if len(s) == 0:
            return []
        
        partitions = []
        
        for i in range(1, len(s)):
        # 找分割点，循环过程中不能使用mem，因为它没有求完，如果用的话会破坏整个递归调用。
            left = s[:i]
            if left not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict)
            for partition in sub_partitions:
                partitions.append(left + " " + partition)
            # 把右半部分加入到左边
        if s in wordDict:
            partitions.append(s)
            
        self.mem[s] = partitions

        
        return partitions
                

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return None
        self.mem = {}
        return self.dfs(s, wordDict)
        
    def dfs(self, s, wordDict):
        if s in self.mem:
            return self.mem[s]
        
        ans = []
        
        if s in wordDict:
            ans.append(s)
        
        for i in range(1, len(s)):
            right = s[i:]
            if right not in wordDict:
                continue
            ans += [w + " " + right for w in self.dfs(s[0:i], wordDict)]
            
        self.mem[s] = ans
        return self.mem[s]


'''
使用记忆化dfs的几个points：

1. 首先要明确dfs函数的意识，一般是有返回值的divide and conquer的思想
2. 使用mem去记录当前s下对应的所有答案
3. 要使用一个ans去记录每次的答案，每一个string对应一个str，所以每次要新建一个
4. 对ans更新时可能要使用循环对每一项进行更新
5. 要去更新mem
6. 分割时要取出right，因为append是往后面添加；因为这个操作是自底向上，先一直遍历到头，再从头往后append；


'''