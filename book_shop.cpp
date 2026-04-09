#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Fast I/O (optional, but recommended for processing large inputs)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num_books, budget;
    if (!(cin >> num_books >> budget)) return 0;

    vector<int> books_prices(num_books);
    for (int i = 0; i < num_books; i++) {
        cin >> books_prices[i];
    }

    vector<int> pages_per_book(num_books);
    for (int i = 0; i < num_books; i++) {
        cin >> pages_per_book[i];
    }

    // Initialize DP table. Size is (num_books + 1) x (budget + 1)
    // We pad an extra row at the top to act as the base case (zero books considered)
    vector<vector<int>> dp(num_books + 1, vector<int>(budget + 1, 0));

    for (int i = 1; i <= num_books; i++) {
        for (int j = 0; j <= budget; j++) {
            
            // i is 1-indexed in the DP table, but our arrays are 0-indexed.
            // Therefore, book[i-1] represents the current book being evaluated.
            int skip = dp[i-1][j];
            int take = 0;
            
            if (j - books_prices[i-1] >= 0) {
                take = dp[i-1][j - books_prices[i-1]] + pages_per_book[i-1];
            }
            
            dp[i][j] = max(skip, take);
        }
    }

    // The final answer is in the bottom-right corner of the DP matrix
    cout << dp[num_books][budget] << "\n";

    return 0;
}