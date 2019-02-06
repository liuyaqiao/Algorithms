class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'bool':
        if not nums:
            return False
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[start] and nums[mid] == nums[end]:
                start += 1
                end -= 1
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if target <= nums[end] and nums[mid] <= target:
                    start = mid
                else:
                    end = mid
        
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False

'''
这是一个二分法的习题：

首先说一下二分法的基本思路：

while start + 1 < end:
    mid = start + (end - start)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        end = mid
    else:
        start = mid

通过这个while循环把整个数组遍历一遍
之后通过一个判断来判断位置

##这里在循环之后会有一个判断，判断到底是哪一个

if nums[start] == target:
    return True
if nums[end] == target:
    return True
return False

这个题有两个trick的地方：
1. 排序数组要考虑每一个mid和处在两段哪一个位置，通过一个if来判断
2. 对于有重复元素的情况，我们需要做一个特殊处理：

类似于
[1,1,1,3,1] 这种情况：
在取mid时，它和nums[start], nums[end]相等；
这时我们无法判断target到底在哪一段，所以需要进行一个start += 1, end -= 1
的操作；

'''
                
        