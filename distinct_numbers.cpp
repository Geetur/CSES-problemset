#include <iostream>
#include <set>

int main() {
	int n;
	std::cin >> n;
	std::set<int> nums;
	for (int i = 0; i < n; ++i) {
		int x;
		std::cin >> x;
		nums.insert(x);
	}
	std::cout << nums.size() << std::endl;
	return 0;
}
