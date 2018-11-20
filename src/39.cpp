class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        
        if (candidates.size() == 0) {
            return res;
        }
        
        vector<int> temp;
        dfs(candidates, target, 0, temp, res);
        return res;
    }
    
    void dfs(vector<int>& candidates, int target, int index, vector<int> &temp ,vector<vector<int>>& res) {
        if (target < 0) {
            return;
        }
        if (target == 0) {
            res.push_back(temp);
        } else {
            for (int i = index; i < candidates.size(); i++) {
                temp.push_back(candidates[i]);
                dfs(candidates, target - candidates[i], i, temp, res);
                temp.pop_back();
            }
        }
    }
};