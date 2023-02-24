from itertools import combinations
n, m = map(int, input().split())
resources = [int(x) for x in input().split()]
planets = {int(x) for x in input().split()}

dp = {0}
ret = 0
for i in range(1, len(resources) + 1):
    for combo in combinations(resources, i):
        total = sum(combo)
        if total in planets:
            planets.discard(total)
            ret += 1
print(ret)