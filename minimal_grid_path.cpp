
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // Optimize standard I/O operations for performance
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // In C++, a vector of strings naturally acts like a 2D grid of characters
    vector<string> string_grid(n);
    for (int i = 0; i < n; ++i) {
        cin >> string_grid[i];
    }

    // Initialize an n x n DP table with empty strings
    vector<vector<string>> dp(n, vector<string>(n, ""));
    
    // Base case
    dp[0][0] = string_grid[0][0];
    string res = dp[0][0];
    // Populate the DP table
    for (int i = 0; i < n; ++i) {
        string local_min = "";
        for (int j = 0; j < n; ++j) {
            if (i == 0 && j == 0) {
                continue;
            } else if (i == 0) {
                dp[i][j] = dp[i][j - 1] + string_grid[i][j];
            } else if (j == 0) {
                dp[i][j] = dp[i - 1][j] + string_grid[i][j];
            } else {
                // min() handles lexicographical string comparison in C++ just like Python
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + string_grid[i][j];
            }
        }
    }

    // Print the bottom-right corner
    cout << dp[n - 1][n - 1] << "\n";

    return 0;
}