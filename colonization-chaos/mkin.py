#!/usr/local/bin/python3
from random import randint, sample

def generate_nums_and_targets(n, target_count, max_num, num_valid, nums=None):
    if nums is None:
        nums = [randint(1, max_num) for _ in range(n)]

    targets = []
    for i in range(target_count):
        if i < num_valid:
            subset_len = randint(1, n)
            targets.append(sum(sample(nums, subset_len)))
            continue
        target = randint(1, 2 * sum(nums))
        targets.append(target)

    return nums, targets


case_num = int(input())
cache_cutoff = 25
dict_cutoff = 45
# 0 and 1 are the sample cases
if case_num == 0:
    print(5, 1)
    nums, targets = generate_nums_and_targets(5, 1, 10, 0)
    print(*nums)
    print(*targets)
elif case_num == 1:
    print(5, 4)
    nums, targets = generate_nums_and_targets(5, 4, 20, 3)
    print(*nums)
    print(*targets)
else:
    # output what should be read in as input by
    # contestant code
    if case_num > cache_cutoff:
        n = 60
    else:
        if case_num < 10:
            n = 5
        else:
            n = 40
    # j = randint(1, 10)
    if case_num > cache_cutoff:
        goal_count = 100_000 
    else:
        goal_count = randint(5, 25)
    # max_num = 10000

    # if case_num > dict_cutoff:
        # n_i = [randint(3000, 10_000) for _ in range(n)]
    def get_goals(goal_lo, goal_hi, n_i, goal_count):
        ret = []
        for i in range(1, goal_count//2):
            total = sum(sample(n_i, min(i, len(n_i)))) + randint(0, 4)
            if total in range(goal_lo, goal_hi + 1):
                ret.append(total)
            # else:
        while len(ret) < goal_count:
            ret.append(randint(0, goal_hi))
        return ret


    if case_num > dict_cutoff:
        n = 1000
        n_i = [randint(100_000, 105_000) for _ in range(n)]
    elif case_num > cache_cutoff:
        n_i = [randint(8000, 50_000) for _ in range(n)]
    else:
        n_i = [randint(4, 50) for _ in range(n)]
    
    if case_num > dict_cutoff:
        # goals = [randint(300_000, 315_000) for _ in range(goal_count)]
        goals = get_goals(300_000, 315_000, n_i, goal_count)
    elif case_num > cache_cutoff:
        # goals = sample(list(range(90_000, 200_000)), goal_count)
        goals = get_goals(90_000, 200_000, n_i, goal_count)
    else:
        # goals = [randint(100, 3_000) for _ in range(goal_count)]
        goals = get_goals(100, 3000, n_i, goal_count)

    # num_valid = randint(0, j)
    print(n, goal_count)
    print(*n_i)
    print(*goals)
    import sys
    print("genned_output", file=sys.stderr)
    # print(n, j)
    # nums, targets = generate_nums_and_targets(n, j, max_num, num_valid)
    # print(*nums)
    # print(*targets)
