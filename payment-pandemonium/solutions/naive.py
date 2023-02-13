def subset_sum(nums, target):
    n = len(nums)
    dp = [[False for j in range(target + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[n][target]

len_nums, len_targets = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))
targets = list(map(int, input().split(' ')))

assert len(nums) == len_nums
assert len(targets) == len_targets

results = [subset_sum(nums, target) for target in targets]
print(sum(results))