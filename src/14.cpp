class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }
        if (strs.size() == 0) {
            return strs[0];
        }
        
        char temp;
        string prefix;
        
        for (int j = 0; j < strs[0].size(); j ++) {
            temp = strs[0][j];
            for (int i = 0; i < strs.size(); i ++) {
                if (j >= strs[i].size() || temp != strs[i][j]) {
                    return prefix;
                }
            }
            prefix.push_back(temp);
        }
        return prefix;
    }
};