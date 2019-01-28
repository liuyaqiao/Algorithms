class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        alp = {'I':1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        sum = alp[s[-1]]
        length = len(s)
        for i in range(length - 1):
            print(i)
            if alp[s[i]] >= alp[s[i + 1]]:
                sum = sum + alp[s[i]]
            else:
                sum = sum - alp[s[i]]
        
        return sum