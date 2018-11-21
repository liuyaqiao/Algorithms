class Solution():
    def maxgift(self, gift):
        if len(gift) == 0:
            return 0
        m = len(gift)
        n = len(gift[0])
        maxValue = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                maxValue[i][j] = gift[i - 1][j - 1] + max(maxValue[i - 1][j], maxValue[i][j - 1])

        print(maxValue[i][j])





if __name__ == '__main__':
    gift = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
    Solution().maxgift(gift)
    # print(gift)