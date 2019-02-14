# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: 'List[NestedInteger]') -> 'int':
        
        if not nestedList:
            return 0
        return self.dfs(nestedList, 1)
        
        
    def dfs(self, nestedList, weight):
        res = 0
        for elem in nestedList:
            if elem.isInteger():
                res = res + weight * elem.getInteger()
            else:
                res = res + self.dfs(elem.getList(), weight + 1)
        return res
                
                
                
'''
一个比较巧妙的dfs习题：

因为它提供的函数getList() 就是在当前的函数下继续搜索的的一个方法：
所以我们这里写dfs的代码：

这里的dfs中有一个分支结构，这也是类似与我们一个返回条件一样；

我们需要抓住递归的三要素：定义，出口和拆解；

定义：
dfs : return nestedList 中所有数字的权重和

出口：
当只是一个数的时候，我们求出和，不需要继续递归

拆解：

res = res + self.dfs(elem.getList(), weight + 1)

这个题目也可以用全局变量来表示res

当然也可以用bfs

'''             
                
                
                