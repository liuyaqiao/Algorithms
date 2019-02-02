class Solution:
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length % 2 == 1:
            return self.findKthSmallest(A, B, length//2 + 1)
        else:
            # return
            return (self.findKthSmallest(A, B, length//2) + self.findKthSmallest(A, B, length//2 + 1))/2
                                         
    def findKthSmallest(self,a,b,k):  
        if len(a) > len(b):
            a, b = b, a
        
        ##递归出口
        if not a:
            return b[k - 1]
        
        if k == 1:
            return min(a[0], b[0])

        
        pa = min(k//2, len(a))
        pb = k - pa
        
        if a[pa - 1] <= b[pb - 1]:
            return self.findKthSmallest(a[pa:], b, k - pa)
        else:
            return self.findKthSmallest(a, b[pb:], k - pb)


'''
这是一个很重要的hard题
找出两个排序好的数组的中位数：首先我们不能用O（n）时间复杂度的算法来计算，这不符合要求。

应该考虑时间复杂度更低的算法：binary search

我们的思路是：
在第一个第二个数组上分别做一个划分，两个划分的元素个数和是k。之后比较这段数字的大小，因为它们
是排序数组，所以可以根据他们最后一位的大小而去掉一半的解。这就是binary search的核心。

之后通过一个递归调用来返回新的子问题。

这里需要注意的是：

1. 递归出口的选取有两个：分别是只有一个list和两个list都只有一个元素的情况，这是我们带入数值计算可得。
2. pa 这里的赋值需要加一个min 考虑到一个数组特别短的情况
3. 注意一下这里k是第几个和index有一些区别
'''