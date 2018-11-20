class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 0) {
            return res;
        }
        
        vector<int> temp;
        vector<int> visited(nums.size());
        for (int i = 0; i < nums.size(); i ++) {
            visited[i] = 0;
        }
        
        dfs(nums, res, visited, temp);
        return res;
        
    }
    
    void dfs(vector<int> &nums, vector<vector<int>> &res, vector<int> visited, vector<int> temp) {
        if (temp.size() == nums.size()) {
            res.push_back(temp);
            return;
        } else {
            for (int i = 0; i < nums.size(); i ++) {
                if (visited[i] == 1) {
                    continue;
                }
                temp.push_back(nums[i]);
                visited[i] = 1;
                dfs(nums, res, visited, temp);
                visited[i] = 0;
                temp.pop_back();
            }
        }
    }
};