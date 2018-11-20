class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        //corner case
        if (nums.size() == 0) {
            return 0;
        }
        if (nums.size() == 1) {
            return 1;
        }
        
        //init
        vector<int> dp(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            dp[i] = 1;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (res < dp[i]) {
                res = dp[i];
            }
        }
        return res;
    }
    
    int max(int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }
};