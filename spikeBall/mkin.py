#!/usr/local/bin/python3
import random
from solutions.sol import dist
def get_coord(coord_bound):
    return (random.randint(-coord_bound, coord_bound), random.randint(-coord_bound, coord_bound))
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(1)
    print(10, 10, 20, 20)
    print(2)
    print(13, 14)
    print(6, 8)
    print(3)
    print(15, 16)
    print(25, 22)
    print(21, 27)
elif case_num == 1:
    print(2)
    print(0, 0, 5, 5)
    print(2)
    print(1, 1)
    print(2, 4)
    print(1)
    print(9, 10)
    print(-100, -100, 5, 5)
    print(1)
    print(0, 0)
    print(1)
    print(5, 20)
else:
    hard_cut_off = 25
    # last_case = 40
    extreme_case_center = 10 ** 17
    test_case_count = random.randint(40, 50)
    # if case_num < hard_cut_off:
    # else:
        # test_case_count = random.randint(7, 9)
    print(test_case_count)
    for t in range(test_case_count):
        center1_x = random.randint(-5000, -4000)
        center1_y = random.randint(-5000, -4000) 
        center2_x = random.randint(200, 500) 
        center2_y = random.randint(200, 500)
        # if case_num == last_case:
        #     center1_x = -extreme_case_center 
        #     center1_y = 0 
        #     center2_x = extreme_case_center
        #     center2_y = 0
        n = random.randint(0, 6)
        m = random.randint(0, 6)
        coord_bound = 50
        if case_num > hard_cut_off and t < 3:
            n = random.randint(97_000, 98_000)
            m = random.randint(97_000, 98_000)
            center2_x = random.randint(4000, 5000) 
            center2_y = random.randint(4000, 5000)
            # coord_bound = 50
        print(center1_x, center1_y, center2_x, center2_y)            
        # if case_num == last_case:
        #     coord_bound = 10**17
        #     offset = 1000
        #     n = 1
        #     m = 1
        #     n_points =[(center1_x + extreme_case_center * 2 + random.randint(-5, 0), center1_y) for _ in range(n)]
        #     m_points =[(extreme_case_center + random.choice([-1, 2]), 0) for _ in range(m)]
        # else:
        n_points =[get_coord(coord_bound) for _ in range(n)]
        m_points =[(40,50) for _ in range(m)]
        if t % 2 == 0:
            n_points.sort(key=lambda x: dist(x, (center1_x, center1_y)))
        else:
            n_points.sort(key=lambda x: dist(x, (center1_x, center1_y)), reverse=True)
        print(n)
        for point in n_points:
            print(*point)
        print(m)
        for point in m_points:
            print(*point)
        

    
