class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums)
        count = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[count - 2]:
                nums[count] = nums[i]
                count += 1
        return count
                

'''
是26题的follow up
同样是双指针，一个指针用来遍历整个数组；
另一个指针来进行判断；
和之前不同的是，起始位置应该有所不同；这里要求可以出现两个数，所以count的值
的初始位置是2，因为前面两个值一定要保留；
因为是升序，所以直接可以使用count - 2处的值和i的值相比较
'''