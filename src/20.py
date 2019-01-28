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
        