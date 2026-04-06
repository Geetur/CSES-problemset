#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// It is good practice to define modulo as a constant globally
const int MOD = 1e9 + 7;

int main() {
    // 1. Fast I/O: Essential for CSES to prevent Time Limit Exceeded (TLE)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num_coins, desired_sum;
    cin >> num_coins >> desired_sum;

    vector<int> coins;
    
    // Read input and filter out coins greater than the desired sum
    for (int i = 0; i < num_coins; ++i) {
        int coin;
        cin >> coin;
        if (coin <= desired_sum) {
            coins.push_back(coin);
        }
    }

    // Sort the coins (matches your Python logic, though strictly optional for this DP)
    sort(coins.begin(), coins.end());

    // 2. DP Array: Using long long to prevent addition overflow before the modulo
    vector<long long> dp(desired_sum + 1, 0);
    dp[0] = 1;

    // 3. Tabulation Logic
    for (int i = 1; i <= desired_sum; ++i) {
        for (int coin : coins) {
            if (i - coin >= 0) {
                // Add the previous state and take the modulo
                dp[i] = (dp[i] + dp[i - coin]) % MOD;
            }
        }
    }

    // 4. Output the result
    // C++ vectors don't support dp[-1] like Python, so we use the exact index or dp.back()
    cout << dp[desired_sum] << "\n";

    return 0;
}