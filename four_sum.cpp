#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long target;
    if (!(cin >> n >> target)) return 0;

    vector<pair<int, long long>> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i].first = i;
        cin >> arr[i].second;
    }

    sort(arr.begin(), arr.end(), [](const pair<int, long long>& a, const pair<int, long long>& b) {
        return a.second < b.second;
    });

    bool found = false;
    for (int i = 0; i < n - 3; ++i) {
        for (int j = i + 1; j < n - 2; ++j) {
            int l = j + 1;
            int r = n - 1;
            while (r > l) {
                long long ii = arr[i].second;
                long long jj = arr[j].second;
                long long ll = arr[l].second;
                long long rr = arr[r].second;
                long long s = ii + jj + ll + rr;

                if (s == target) {
                    cout << arr[i].first + 1 << " " << arr[j].first + 1 << " " 
                         << arr[l].first + 1 << " " << arr[r].first + 1 << "\n";
                    found = true;
                    break;
                } else if (s > target) {
                    r -= 1;
                } else {
                    l += 1;
                }
            }
            if (found) {
                break;
            }
        }
        if (found) {
            break;
        }
    }
    
    if (!found) {
        cout << "IMPOSSIBLE\n";
    }

    return 0;
}