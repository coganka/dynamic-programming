def lis(nums, i=0, prev_idx=-1, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i, prev_idx) in lookup:
        return lookup[(i, prev_idx)]
    if i == len(nums):
        return 0
    elif prev_idx != -1 and nums[i] < nums[prev_idx]:
        return lis(nums, i+1, prev_idx, lookup)
    lookup[(i,prev_idx)] = max(1 + lis(nums, i+1, i, lookup), lis(nums, i+1, prev_idx, lookup))
    return lookup[(i,prev_idx)]

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis(nums))