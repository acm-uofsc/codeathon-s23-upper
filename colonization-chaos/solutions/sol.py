n, m = map(int, input().split())
resources = [int(x) for x in input().split()]
planets = [int(x) for x in input().split()]

dp = {0}
highest_in_planets = max(planets)
for value in resources:
    for existing in list(dp):
        if existing + value <= highest_in_planets:
            dp.add(existing + value)
print(sum(total in dp for total in planets))