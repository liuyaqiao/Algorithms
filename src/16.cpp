class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if (nums.size() < 3) {
            return 0;
        }        
        
        int res = 0;
        int minVal = INT_MAX;
        int diff = 0;
        int temp = 0;
        int left = 0;
        int right = 0;
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 2; i ++) {
            left = i + 1;
            right = nums.size() - 1;
            while (left < right) {
                temp = nums[i] + nums[left] + nums[right];
                diff = abs(temp - target);
                if (diff < minVal) {
                    minVal = diff;
                    res = temp;
                }
            
                if (temp > target) {
                    right --;
                } else if (temp < target) {
                    left ++;
                } else {
                    return target;
                }
            }
        }
        return res;
        
    }
};