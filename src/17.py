class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # print(digits)
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        digit_str = str(digits)
        if len(digits) == 0 :
            return res
        # print(digit_str[1])

        self.dfs(d, res, '', 0, digit_str)
        # print(res)
        return res

    def dfs(self, d, res, temp, index, digits):
        if len(temp) == len(digits):
            res.append('' + temp)
            return
        else:
            for i in d[digits[index]]:
                # print('digits[i] = ',digits[index])
                temp += i
                self.dfs(d, res, temp, index + 1, digits)
                temp = temp[:-1]