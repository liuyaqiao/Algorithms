# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        p = self.Parition(0, len(numbers) - 1, numbers)
        left = 0
        right = len(numbers) - 1
        mid = len(numbers)/2 + 1
        while True:
            length = p + 1
            if length > mid:
                right -= 1
                p = self.Parition(left, right, numbers)
            elif length < mid:
                left += 1
                p = self.Parition(left, right, numbers)
            else:
                if self.checkMoreThanHalf(numbers[p], numbers) == True:
                    return numbers[p]
                else:
                    return 0
            
    def Parition(self, left, right, numbers):
        #return parition position
        pivot = numbers[right]
        p = left
        for now in range(left, right):
            if numbers[now] < pivot:
                numbers[now], numbers[p] = numbers[p], numbers[now]
                p += 1
        numbers[p], numbers[right] = numbers[right], numbers[p]
        return p
    
    def checkMoreThanHalf(self, result, numbers):
        time = 0
        for i in range(0, len(numbers)):
            if numbers[i] == result:
                time += 1
        if time >= len(numbers)/2 + 1:            
            return True
        else:
            return False