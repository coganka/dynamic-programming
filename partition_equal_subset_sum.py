def partition_equal_subset_sum(nums):
    if sum(nums) % 2 != 0:
        return False
    lookup = {}
    target = sum(nums) // 2
    def helper(nums, cur_sum, target, i, lookup):
        if (cur_sum, i) in lookup:
            return lookup[(cur_sum, i)]
        elif i == len(nums) or cur_sum > target:
            return False
        elif cur_sum == target:
            return True
        else:
            lookup[(cur_sum, i)] = helper(nums, cur_sum + nums[i], target, i+1, lookup) or helper(nums, cur_sum, target, i+1, lookup)
            return lookup[(cur_sum, i)]
    return helper(nums, 0, target, 0, lookup)

nums = [1, 5, 11, 5]
print(partition_equal_subset_sum(nums))