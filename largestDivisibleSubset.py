def largestDiv(nums):
    nums.sort()
    lookup = {}
    def dfs(i,prev_idx):
        if (i,prev_idx) in lookup:
            return lookup[(i,prev_idx)]
        if i == len(nums):
            return []
        without = dfs(i+1,prev_idx)
        withCur = []
        if prev_idx == -1 or nums[i] % nums[prev_idx] == 0:
            withCur = [nums[i]] + dfs(i+1,i)
        lookup[(i,prev_idx)] = withCur if len(withCur) > len(without) else without
        return lookup[(i,prev_idx)]
    return dfs(0,-1)

nums = [1,2,3]
print(largestDiv(nums))