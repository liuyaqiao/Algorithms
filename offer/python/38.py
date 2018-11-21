# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        result = []
        visited = [0] * len(ss)
        if ss == None or len(ss) == 0:
            return result
        self.dfs('', ss, result, visited)
        return result
        
        
    def dfs(self, subset, ss, result, visited):
        #return all the permutation which begins with subset
        if len(subset) == len(ss):
            result.append(subset)
            
        for i in range(0, len(ss)):
            if visited[i] == 1:
                continue
            
            if i != 0 and ss[i] == ss[i - 1] and visited[i - 1] == 0:
                continue
            
            subset += ss[i]
            visited[i] = 1
            self.dfs(subset, ss, result, visited)
            subset = subset[0:len(subset)-1] + ''
            visited[i] = 0

    