#!/usr/local/bin/python3
from random import randint, sample

def generate_nums_and_targets(n, target_count, max_num, num_valid):
    nums = [randint(1, max_num) for _ in range(n)]

    targets = []
    for i in range(target_count):
        if i < num_valid:
            subset_len = randint(1, n)
            targets.append(sum(sample(nums, subset_len)))
            continue
        target = randint(1, 10 * max_num)
        targets.append(target)

    return nums, targets


case_num = int(input())
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
    n = randint(10, 100)
    j = randint(1, 100)
    max_num = 10000
    num_valid = randint(0, j)
    print(n, j)
    nums, targets = generate_nums_and_targets(n, j, max_num, num_valid)
    print(*nums)
    print(*targets)
