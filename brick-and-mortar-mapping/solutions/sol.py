from math import dist
n, m = map(int, input().split())
def parse_coords():
    spots = input().split()
    return [tuple(map(int, coord.split(","))) for coord in spots]
stores = parse_coords()
people = parse_coords()
for i in range(m):
    closest = min(stores, key=lambda x: dist(people[i], x))
    print(*closest, sep=',')