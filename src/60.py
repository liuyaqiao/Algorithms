class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i + 1 for i in range(n)]
        res = []
        fact = [0 for _ in range(n)]
        fact[0] = 1
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
            
        k = k - 1
        for i in range(n, 0, -1):
            index = k // fact[i - 1]
            k = k % fact[i - 1]
            res.append(nums[index])
            nums.remove(nums[index])
        
        result = ''
        
        for s in res:
            result = result + str(s)

        return result

'''
这道题的意思是找第几个排列，我们当然可以找出所有的排列之后直接去取第几个。但是这样做的时间复杂度会很高，所以我们
观察到，一个全排列是由n个n-1个数字的全排列组成。所以我们可以得出n个数字的全排列是n！个。所以针对这个题我们有了
解题方法，我们首先找出第k个全排列的开头数字是几，之后在考察它第二的数字是几这样的规律去计算。

所以我们需要几个list
第一个要储存数字 nums
第二个要储存全排列的个数 fact
我们用k去除n-1个全排列的个数的尚就可以知道这个全排列的首位数字是多少
再用余数可以得到新的k

这个题要注意的是：
k的取值问题，k的意思是第几个，是从1开始的，而我们的数组都是从0开始的。
所以为了简单期间，这里k做了-1处理。

从list转换成''的时候，如果list中是str的时候，我们可以用''.join(). 
如果不是的话，我们还是循环比较好。

'''