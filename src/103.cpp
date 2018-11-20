/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (root == NULL) {
            return result;
        }
        
        queue<TreeNode *> queue;
        queue.push(root);
        int level = 1;
        while (!queue.empty()) {
            int size = queue.size();
            vector<int> currentlevel;
            for (int i = 0; i < size; i++)
            {
                TreeNode *head = queue.front();
                queue.pop();
                currentlevel.push_back(head->val);
                if (head->left != NULL) {
                    queue.push(head->left);
                }
                if (head->right != NULL) {
                    queue.push(head->right);
                }
            }
            if (level == -1) {
            reverse(currentlevel.begin(), currentlevel.end());
            }
            level = -level;
            result.push_back(currentlevel);
        }
    return result;
    }
    
};