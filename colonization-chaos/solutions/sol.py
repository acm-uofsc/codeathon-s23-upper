def subset_sum(nums, target):
    n = len(nums)
    dp = [False for j in range(abs(target) + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(abs(target), 0, -1):
            if nums[i - 1] <= j and j - nums[i - 1] >= 0:
                dp[j] = dp[j] or dp[j - nums[i - 1]]
    return dp[abs(target)]



len_nums, len_targets = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))
targets = list(map(int, input().split(' ')))

assert len(nums) == len_nums
assert len(targets) == len_targets

results = [subset_sum(nums, target) for target in targets]
print(sum(results))