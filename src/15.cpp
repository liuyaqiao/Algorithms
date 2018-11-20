class Solution {
public:
    void twoSum(int left, int right, int target, vector<int> &numbers, vector<vector<int>> &result)
    {
        while (left < right) {
            if (numbers[left] + numbers[right] == target) {
                vector<int> Three;
                Three.push_back(-target);
                Three.push_back(numbers[left]);
                Three.push_back(numbers[right]);
                result.push_back(Three);
                
                left++;
                right--;
                
                while (left < right && numbers[left] == numbers[left - 1]) {
                    left++;
                }
                while (left < right && numbers[right] == numbers[right + 1]) {
                    right--;
                }
                
            } else if (numbers[left] + numbers[right] < target) {
                left++;
            } else {
                right--;
            }
        }
    }
     
    vector<vector<int>> threeSum(vector<int> &numbers) {
        // write your code here
        vector<vector<int>> result;
        if (numbers.size() < 3) {
            return result;
        }
        
        sort(numbers.begin(), numbers.end());

        for (int i = 0; i < numbers.size(); i++) {
            if (i > 0 && numbers[i] == numbers[i - 1]) {
                continue;
            }
            int target = -numbers[i];
            int left = i + 1;
            int right = numbers.size() - 1;
            twoSum(left, right, target, numbers, result);
        }
        return result;
    }
};