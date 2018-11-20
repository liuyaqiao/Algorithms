#include <iostream>
#include <vector>
#include <cmath>

class Solution {
public:
    int coinChange(std::vector<int> & coins, int amount) {
        if (amount == 0) {
            return 0;
        }

        std::vector<int> dp(amount + 1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i ++) {
            dp[i] = amount + 1;
        }

        for (int i = 0; i < coins.size(); i++) {
//            printf("%d", coins[i]);
            if (coins[i] < amount) {
                dp[coins[i]] = 1;
            }
        }



        for (int i = 1; i < amount + 1; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (i >= coins[j]) {
                    int temp = 0;
                    temp = dp[i - coins[j]] + 1;
                    dp[i] = min(dp[i], temp);
                }
            }
        }

        if (dp[amount] == amount + 1) {
            return -1;
        }
        return dp[amount];
    }

    int min(int & a, int & b) {
        if (a >= b) {
            return b;
        } else {
            return a;
        }

    }
};


int main() {
//    std::cout << "Hello, World!" << std::endl;
    int amount = 1;
    std::vector <int> coins(1);
    coins = {1};
    Solution s;
    int result;
    result = s.coinChange(coins, amount);
    printf("%d", result);


}