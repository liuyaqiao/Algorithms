class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        
        if (candidates.size() == 0) {
            return res;
        }
        vector<int> temp;
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, res, 0, temp);
        return res;
        
    }
    
    void dfs(vector<int> &candidates, int target, vector<vector<int>> &res, int index, vector<int> temp) {
        if (target < 0) {
            return;
        }
        if (target == 0) {
            res.push_back(temp);
        } else {
            for (int i = index; i < candidates.size(); i ++) {
                if (i > index && candidates[i] == candidates[i - 1]) {
                    continue;
                }
                temp.push_back(candidates[i]);
                dfs(candidates, target - candidates[i], res, i + 1, temp);
                temp.pop_back();
            }
        }
    }
};