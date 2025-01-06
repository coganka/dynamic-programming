def subset_sum(nums, k, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i,k) in lookup: # already seen it
        return lookup[(i,k)]
    if k == 0: # sum got to target
        return 1
    elif k < 0 or i == len(nums): # bounds checking
        return 0
    else:
        # take it and move or dont take it and move, add bc we are counting
        lookup[(i,k)] = subset_sum(nums, k-nums[i], i+1, lookup) + subset_sum(nums, k, i+1, lookup)
        return lookup[(i,k)]
    
nums = [1,2,3,1,4]
print(subset_sum(nums, 6))