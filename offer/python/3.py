# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        index = [0] * len(numbers)
        for i in range(len(numbers)):
            index[numbers[i]] += 1
        
        for i in range(len(index)):
            if index[i] > 1:
                duplication[0] = i
                return True
        return False