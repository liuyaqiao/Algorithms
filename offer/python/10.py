# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        Fib_0 = 0
        Fib_1 = 1
        if n == 0:
            return Fib_0
        if n == 1:
            return Fib_1

        fibN, fib1, fib2 = 0, 1, 0
        for i in range(2,n + 1):
            #这里从0开始 所以目标是n个数 循环应该包括n
            fibN = fib1 + fib2
            fib2 = fib1
            fib1 = fibN
        return fibN