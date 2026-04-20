#include <iostream>
#include <set>
#include <cmath>
#include <algorithm>


int main() {

    int n;
    std::cin >> n;

    std::multiset<int> towers;
    for (int i = 0; i < n; ++i) {
        int height;
        std::cin >> height;
        auto greater_it = towers.upper_bound(height);
        if (greater_it == towers.end()) {
            towers.insert(height);
        }
        else {
            towers.erase(greater_it);
            towers.insert(height);
        }
        }
        std::cout<<towers.size() << std::endl; 
    return 0;
}
