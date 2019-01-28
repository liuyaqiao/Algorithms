class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        
        hashMap = {}
        #key 'sorted str' value 'index in dict'
        res = []
        
        for str in strs:
            s = ''.join(sorted(str))
            if s in hashMap:
                res[hashMap[s]].append(str)
            else:
                new = []
                new.append(str)
                index = len(res)
                res.append(new)
                hashMap[s] = index
        return res


'''
这个题要求我们将list中的字符串按照各自包含的char的不同而分开；

这种题我们很自然的想到要使用hashmap的方法，所以难点再也我们如
何去构造hashmap；

这里用的一种方法是，不同的string排序之后得到的string是相同的，
所以我们可以利用这个性质，巧妙的是，它的key值是当前储存strings
的数组在res中的index。

这里一个比较常用的hashmap查找的结构是：

if s in hashMap:
    '''如果找到进行的操作'''
else:
    '''如果找不到之后进行的操作'''

同时这种hashmap中value映射的方法也要多积累注意；

'''