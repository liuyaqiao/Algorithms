class Solution:
    def numTrees(self, n: 'int') -> 'int':
        
        #f(n) = f(0) * f(n - 1) + f(1) * f(n - 2) + ... + f(n - 1) * f(0)
        res = [0 for i in range(n + 1)]
        res[0] = 1
        
        for i in range(1, n + 1):
            for j in range(i):
                res[i] = res[i] + res[j] * res[i - 1 - j]
        ##这里j表示左孩子
        return res[n]
            
'''
首先判断这是一个dp的问题：

要求的个数与之前的个数有关；我们可以看出，状态方程如下：

f(n) = f(0) * f(n - 1) + f(1) * f(n - 2) + ... + f(n - 1) * f(0)

这里我们把f(n) 写成一个状态量； res[n]

res[j] 表示left child res[i - 1 - j] 表示right child

而i表示总的节点数；

'''