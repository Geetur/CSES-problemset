import sys
n = int(sys.stdin.readline())

nums = len(set(map(int, sys.stdin.readline().split())))

print(nums)