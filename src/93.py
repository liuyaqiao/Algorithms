class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        
        result = []
        self.dfs(s, 0, result, '')
        return result
    
    def dfs(self, s, index, result, ip):
        if index == 4:
            if s == '':
                result.append(ip[1:])
                #去掉.
            return
        
        for i in range(1, 4):
            #可以取几个字符
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], index + 1, result, ip + '.' + s[:i])
            else:
                continue
            if s[0] == '0':
                break
                
                        

'''
关于字符串重的backtracking

1. 把参数的改变写到函数调用之中，则不需要写回溯的过程，因为函数return的过程包含了回溯的过程。
2. 有关字符串的递归，我们常用的是直接改变字符串，例如s[1:]这种形式，写法会简单一些
3. 注意这个题的return条件

在和list有关的时候，多用临时变量来储存和pop，这里直接写在函数调用中更方便。

'''