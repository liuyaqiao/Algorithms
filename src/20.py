class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        helper = {'{' : '}', '[' : ']', '(':')'}
        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            if i == '}' or i == ']' or i == ')':
                if len(stack) == 0:
                    return False
                elif i == helper[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
'''
这个题的意思是让我们验证括号是不是完整；我们自然想到使用stack的数据结构
首先需要一个map来提供左右括号的映射；之后对input进行循环，如果是做括号做入栈操作；
如果是右括号，和栈顶元素匹配则出栈，不匹配则返回False。
最后匹配的关键与否在于stack的长度是不是为0
'''