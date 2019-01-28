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

'''
这个题的大意是让我们根据罗马字母去写书int的大小，输入是一个字符串，而输出是对应整数的大小。

思路：

根据题意是按照string的顺序去读取每一个char，按照它和下一位的大小去决定是加减。
思路比较简单，需要一个map来提供罗马字母到数字的映射，再通过一个循环去比较。
这里要注意的是，再循环比较大小的时候要注意一下越界问题，这里的处理是先把sum设置成最后一个元素。

'''