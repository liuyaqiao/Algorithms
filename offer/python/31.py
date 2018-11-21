# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) == 0 or len(popV) == 0:
            return False
        stack = []

        for i in range(len(pushV)):
            stack.append(pushV[i])
            while len(stack) != 0 and stack[-1] == popV[0]:
                stack.remove(stack[-1])
                popV.remove(popV[0])
        if len(stack) == 0:
            return True
        return False