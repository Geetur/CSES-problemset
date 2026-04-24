#include <algorithm>
#include <iostream>
#include <set>

int main() {
    int n;
    std::cin >> n;

    std::multiset<int> alive;
    for (int i = 1; i <= n; ++i) {
        alive.insert(i);
    }

    auto it = alive.begin();
    std::advance(it, 1);

    while (alive.size() > 1) {
        std::cout << *it << " ";

        it = alive.erase(it);

        if (it == alive.end())
            it = alive.begin();

        std::advance(it, 1);

        if (it == alive.end())
            it = alive.begin();
    }
    std::cout << *it << " ";
    return 0;
}







