import sys
from collections import deque

num_applicants, num_apartments, max_difference = map(int, sys.stdin.readline().split())

desired_size = deque(sorted(list(map(int, sys.stdin.readline().split()))))

apartment_sizes = deque(sorted(list(map(int, sys.stdin.readline().split()))))

ans = 0
while desired_size:
    applicant = desired_size.popleft()
    while apartment_sizes:
        candidate = apartment_sizes.popleft()
        if candidate - max_difference <= applicant <= candidate + max_difference:
            ans += 1
        else:
            if candidate > applicant:
                apartment_sizes.appendleft(candidate)
            elif applicant > candidate:
                desired_size.appendleft(applicant)
        break
        
print(ans)


