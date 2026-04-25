#include <iostream>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

// Define the ordered_set which supports random access by index
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

int main() {
    int n, k;
    if (!(cin >> n >> k)) return 0;

    ordered_set alive;
    for (int i = 1; i <= n; ++i) {
        alive.insert(i);
    }

    int pos = 0;
    while (!alive.empty()) {
        // Calculate exact target index mathematically
        pos = (pos + k) % alive.size();
        
        // Find the iterator at that exact index in O(log N) time
        auto it = alive.find_by_order(pos);
        
        cout << *it << " ";
        alive.erase(it); // Erase in O(log N) time
    }
    
    cout << "\n";
    return 0;
}

