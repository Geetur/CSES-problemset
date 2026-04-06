#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Using a very large integer instead of float("inf")
const int INF = 1e9; 

int main() {
    // Fast I/O operations (highly recommended in C++)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num_choices, target;
    // Read input until EOF
    if (!(cin >> num_choices >> target)) return 0;

    vector<int> choices(num_choices);
    for (int i = 0; i < num_choices; ++i) {
        cin >> choices[i];
    }

    // Creating the 2D DP vector, initialized to INF
    vector<vector<int>> dp(num_choices + 1, vector<int>(target + 1, INF));

    // Base case: target 0 takes 0 coins
    for (int i = 0; i <= num_choices; ++i) {
        dp[i][0] = 0;
    }

    // Filling the DP table exactly as you did in Python
    for (int i = num_choices - 1; i >= 0; --i) {
        for (int j = 1; j <= target; ++j) {
            int skip = dp[i + 1][j];
            int take = INF;
            if (j - choices[i] >= 0) {
                if (dp[i][j - choices[i]] != INF) {
                    take = 1 + dp[i][j - choices[i]];
                }
            }
            dp[i][j] = min(skip, take);
        }
    }

    int ans = dp[0][target];

    // Check if the answer is still INF or 0
    if (ans >= INF || ans == 0) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}



