class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
                
        return count


'''
这是一个同向双指针的习题，一个指针去扫描整个数组；
另一个去寻找相等的数；
对比linkedlist的操作，这里需要做的是和前一个进行对比；

'''