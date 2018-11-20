class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        } 
        if (nums.size() == 0) {
            return nums[0];
        }
        
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        
        for (int i = 1; i < nums.size(); i ++) {
            dp[i] = max(dp[i - 1] + nums[i], nums[i]);
        }
        
        int max_val;
        max_val = INT_MIN;
        
        for (int i = 0; i < nums.size(); i ++) {
            if (max_val < dp[i]) {
                max_val = dp[i];
            }
        }
        
        return max_val;
    }
    
    int max(int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }
};