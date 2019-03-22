class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 0:
            return []
        result = []
        self.dfs(result, "", n, n)
        return result
    
    def dfs(self, result, temp, left, right):
        if left > right:
            return
        
        if left == 0 and right == 0:
            result.append(temp)
            return
        
        if left > 0:
            self.dfs(result, temp + "(", left - 1, right)
        
        if right > 0:
            self.dfs(result, temp + ")", left, right - 1)


'''
backtracking：

注意的点：
1. 用left > right 来限制不符合规则的条件
2. backtracking的规则就是在函数调用中加入temp + "C"的变量，这时可以省略掉回溯
的过程

'''