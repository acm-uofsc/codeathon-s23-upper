#!/usr/local/bin/python3
from random import randint, sample
from itertools import combinations
import math


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def same_distance(customers, stores, x, y):
    ops = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for customer in customers:
        cx, cy = customer
        dx = abs(x - cx)
        dy = abs(y - cy)
        perms = [(cx + op[0] * dx, cy + op[1] * dy) for op in ops]
        swapped_perms = [(cx + op[0] * dy, cy + op[1] * dx) for op in ops]
        perms = perms + swapped_perms
        for perm in perms:
            if perm in customers:
                return True
    return False


def gen_stores(n, min_c=-10000, max_c=10000):
    # n is the number of coords
    # coords = []
    # for i in range(n):
    #     x = randint(min_c, max_c)
    #     y = randint(min_c, max_c)
    #     # dist = euclidean_distance(customers[0], (x,y))

    #     while (x,y) in coords:
    #     # while (x,y) in coords or same_distance(customers, coords, x, y):
    #         x = randint(min_c, max_c)
    #         y = randint(min_c, max_c)
    #         # dist = euclidean_distance(customers[0], (x,y))
    #     coords.append((x, y))
    #     # distances.add(dist)
    coords = sample(list(combinations(range(min_c,max_c),2)), n)
    return coords



def gen_customers(n, stores, min_c=-10000, max_c=10000):
    # n is the number of coords
    coords = []
    for i in range(n):
        x = randint(min_c, max_c)
        y = randint(min_c, max_c)
        while (x,y) in coords or (x,y) in stores:
            x = randint(min_c, max_c)
            y = randint(min_c, max_c)
        coords.append((x, y))
    return coords


def gen_test_case(n, m, min_c=-500, max_c=500):
    stores = gen_stores(n, min_c=min_c, max_c=max_c)
    customers = gen_customers(m, stores, min_c=min_c, max_c=max_c)
    return customers, stores


case_num = int(input())
if case_num == 0:
    print(10, 1)
    customers, stores = gen_test_case(10, 1, min_c=-10, max_c=10)
    print(*[str(x) + ',' + str(y) for x, y in stores])
    print(*[str(x) + ',' + str(y) for x, y in customers])
elif case_num == 1:
    print(10, 1)
    customers, stores = gen_test_case(10, 2, min_c=-10, max_c=10)
    print(*[str(x) + ',' + str(y) for x, y in stores])
    print(*[str(x) + ',' + str(y) for x, y in customers])
elif case_num <= 35:
    n = randint(10, 10**4)
    m = randint(1, 100)
    print(n, m)
    stores = gen_stores(n, min_c=-500, max_c=-1)
    customers = gen_customers(m, stores, min_c=0, max_c=1000)
    for i in range(n):
        if i < n-1:
            print(*stores[i], sep=',', end=' ')
        else:
            print(*stores[i], sep=',')
    print(*[str(x) + ',' + str(y) for x, y in customers])
else:
    n = randint(1000, 10**4)
    m = randint(5000, 10000)
    print(n, m)
    customers = gen_stores(m, min_c=-1000, max_c=0)
    stores = gen_customers(n, customers, min_c=1, max_c=1000)
    for i in range(n):
        if i < n-1:
            print(*stores[i], sep=',', end=' ')
        else:
            print(*stores[i], sep=',')
    print(*[str(x) + ',' + str(y) for x, y in customers])