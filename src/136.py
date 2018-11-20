class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numHash = set()
        for item in nums:
            if item not in numHash:
                numHash.add(item)
            else:
                numHash.remove(item)
                
        return numHash.pop()