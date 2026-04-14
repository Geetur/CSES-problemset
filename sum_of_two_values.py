n, target_sum = map(int, input().split())

# 1. Read the array normally
raw_arr = list(map(int, input().split()))

# 2. Store as (value, original_1_based_index) and THEN sort
arr = sorted([(val, i + 1) for i, val in enumerate(raw_arr)])

l, r = 0, n - 1
found = False

while l < r:
    # Look at the 'value' part of the tuple (index 0)
    current_sum = arr[l][0] + arr[r][0]
    
    if current_sum == target_sum:
        # Print the 'original_index' part of the tuple (index 1)
        print(arr[l][1], arr[r][1])
        found = True
        break
    elif current_sum > target_sum:
        r -= 1
    else:
        l += 1

if not found:
    print("IMPOSSIBLE")

