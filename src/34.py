class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        
        ##to find first position
        start = 0
        end = len(nums) - 1
        result = []
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            ##XXOOXX1,2,2,2,3,
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[start] == target:
            result.append(start)
        elif nums[end] == target:
            result.append(end)
        else:
            result.append(-1)
        
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            ##XXOOXX1,2,2,2,3,
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
                
            # print('start, end', start, end)
            
        if nums[end] == target:
            result.append(end)
        elif nums[start] == target:
            result.append(start)
        else:
            result.append(-1)
        
        return result

        
            
            