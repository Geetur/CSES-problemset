#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, target_sum;
  
    if (!(cin >> n >> target_sum)) return 0;
 
    unordered_map<int, int> seen;
    bool found = false;

    for (int i = 0; i < n; ++i) {
        int num;
        cin >> num;

        int complement = target_sum - num;
        
        if (seen.count(complement)) {

            cout << seen[complement] << " " << i + 1 << "\n";
            found = true;
            break;
        } else {
            
            seen[num] = i + 1;
        }
    }

    if (!found) {
        cout << "IMPOSSIBLE\n";
    }

    return 0;
}