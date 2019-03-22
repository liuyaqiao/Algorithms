class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = collections.defaultdict(int)
        used_nums = []
        for item in nums:
            if item in used_nums:
                continue
            
            used_nums.append(item)
            
            left = hashset[item - 1]
            right = hashset[item + 1]
            
            if left > 0 and right > 0:
                hashset[item] = left + right + 1
                hashset[item - left] = left + right + 1
                hashset[item + right] = left + right + 1
            elif  left > 0:
                hashset[item] = hashset[item - left] + 1
                hashset[item - left] += 1
            elif right > 0:
                hashset[item] = hashset[item + right] + 1
                hashset[item + right] += 1
            else:
                hashset[item] = 1
            
        return max(hashset.values())
'''
数组的题一般都要O(n)的时间复杂度，我们可以使用一个hashmap去存放
一些信息，然后通过得到的数据去更新；

这里用一个数组used_nums 去重

'''