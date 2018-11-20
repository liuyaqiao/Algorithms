class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        res = ''
        a = '1'
        for i in range(1, n):
            res = self.count(a)
            a = res
        return res
    
    def count(self, a):
        i = 0
        res = ''
        while i < len(a):
            cnt = 1
            while i != len(a) - 1 and a[i] == a[i + 1]:
                cnt += 1
                i += 1
            
            res = res + str(cnt) + str(a[i])
            i += 1
            
        return res