class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ##奇偶正负
        # 二分法
        
        if n == 0 or x == 1:
            return 1
        
        if n == 1:
            return x
        
        if n < 0:
            return 1/(x * self.myPow(x, -(n + 1)))
        
        res = 1.0
        
        while n > 1:
            if n % 2 == 1:
                res *= x
            x = x * x
            n = n // 2

        res *= x
        return res 

'''
此题让我们实现一个pow的函数，我们很明显不能直接去挨个乘每一项，这是一个
复杂度超过要求的算法；
所以我们要考虑一个新的算法，可以发现有如下规律：
2^9
res nums pow
1    2    9
2*2  4    4
2*2  4*4  2
2*2  16*16 1

可以看到这是一个二分法，返回pow等于奇数的情况，res乘上一个nums，使得pow变为偶数再进行操作。
具体的操作是，num每次做乘法，而pow则每次减小一半，直到pow的大小为1.

如果pow是负数，一般来说是1/pow(x, -n)

因为负数最小值比正数最小数多一个：eg: [−2^31, 2^31 − 1]

1/(x * self.myPow(x, -(n + 1)))

负数的最小值不能通过取相反数得到正数的最大值；当然这里不做这样的操作也可以AC

'''