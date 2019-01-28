class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        
        hashMap = {}
        #key 'sorted str' value 'index in dict'
        res = []
        
        for str in strs:
            s = ''.join(sorted(str))
            if s in hashMap:
                res[hashMap[s]].append(str)
            else:
                new = []
                new.append(str)
                index = len(res)
                res.append(new)
                hashMap[s] = index
        return res