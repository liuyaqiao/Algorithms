class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 0
        result = [0 for i in range(len(digits) + 1)]
        
        for i in range(len(digits) - 1, -1, -1):           
            if i == len(digits) - 1:
                flag = (digits[i] + 1) // 10
                digits[i] = (digits[i] + 1) % 10
            else:
                temp = digits[i]
                digits[i] = (digits[i] + flag) % 10
                flag = (temp + flag) // 10

            if i == 0 and flag == 1:
                result = [0 for i in range(len(digits) + 1)]
                result[0] = 1
                return result
        return digits
        