class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        result = []
        self.dfs(s, result, [])
        return result
        
    def dfs(self, s, result, temp):
        if len(s) == 0:
            result.append(temp)
            return
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.isValid(prefix) == True:
                self.dfs(s[i:], result, temp + [prefix])
                
    def isValid(self, s):
        return s == s[::-1]
    
'''
这是一个backtracking的重要习题：

关键点在于：

1. 截取字符串
2. 在dfs函数调用中更改变量可以省略回溯的过程
3. return的返回条件
4. 模拟整个过程
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        
        result = []
        self.dfs(s, [], result)
        return result
        
    def dfs(self, s, temp, result):
        if len(s) == 0:
            result.append(temp + [])
            return
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.isValid(prefix) == True:
                temp.append(prefix)
                self.dfs(s[i:], temp, result)
                temp.pop()
        
    def isValid(self, s):
        return s == s[::-1]


'''
函数形参的两种写法，用+会新建一个数组，这样可以永久的保存，而用append的话
则只是对当前的list做操作，会导致保存在result中的数组为空
总之类似的题，要新建一个list去保存，都需要一个+的存在。

'''