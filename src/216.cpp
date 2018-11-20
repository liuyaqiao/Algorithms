class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        vector<int> candidates = {1,2,3,4,5,6,7,8,9};
        for (int i = 0; i < candidates.size(); i ++) {
            printf("%d,", candidates[i]);
        }
        
        vector<int> temp;
        dfs(candidates, n, temp, res, 0, k);
         
        return res;
    }
    
    void dfs(vector<int> &candidates, int target, vector<int> &temp, vector<vector<int>> &res, int index, int k) {
        if (temp.size() > k || target < 0) {
            return;
        }
        if (temp.size() == k && target == 0) {
            res.push_back(temp);
        } else {
            for (int i = index; i < candidates.size(); i ++) {
                temp.push_back(candidates[i]);
                dfs(candidates, target - candidates[i], temp, res, i + 1, k);
                temp.pop_back();
            }
        }
        
    }
};