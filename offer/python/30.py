# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.subStack = []
    
    def push(self, node):
        # write code here
        if len(self.subStack) == 0:
            self.subStack.append(node)
        else:
            if node < self.subStack[len(self.subStack) - 1]:
                self.subStack.append(node)
            else:
                self.subStack.append(self.subStack[-1])
        self.stack.append(node)
    
    def pop(self):
        # write code here
        if len(self.stack) == 0 or len(self.subStack) == 0:
            return None
        self.stack.pop()
        self.subStack.pop()     
        
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.subStack[-1]


#取最后一个元素list[-1] !!!