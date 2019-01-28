import sys
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #corner case
        if len(nums) == 0:
            return
        
        firstSmall = -1
        firstLarge = -1
        
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i] :
                firstSmall = i
                break
        if firstSmall == -1:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, firstSmall, -1):
                if nums[i] > nums[firstSmall]:
                    firstLarge = i
                    break
            nums[firstSmall], nums[firstLarge] = nums[firstLarge], nums[firstSmall]
        # print(firstSmall, firstLarge)
            self.reverseList(firstSmall + 1, len(nums) - 1, nums)
        
        
        
    def reverseList(self, i, j, nums):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
'''
这个题要求我们找出下一个排列：

我们发现下一个排列的思路是：

1 2 7 4 3 1
1 2 7 4 3 1
1 3 7 4 2 1
1 3 1 2 4 7

找到当前最后一个顺序增大的数的前一项，再将他于后从向前数第一个大于它的数交换。之后对剩余的部分
做一个转置操作，可以得到新的一个排列即是我们要的下一个排列。

这道题的难点主要是这个思路：

之后我们注意一下寻找最后一个增大序列的前数，可以从末尾开始找。这是一个小技巧


'''