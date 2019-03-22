class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0
        hashset = set()
        for char in J:
            hashset.add(char)
            
        count = 0
        for char in S:
            if char in hashset:
                count += 1
                
        return count