#!/usr/local/bin/python3
import random
from collections import defaultdict as dd
case_num = int(input())
# 0 and 1 are the sample cases
dirs = {
    0 : "^",
    1 : ">",
    2 : "v",
    3 : "<",
}
if case_num == 0:
    print(4, 2)
    print(">>>v")
    print("v<><")
elif case_num == 1:
    print(5, 3)
    print(">v>>v")
    print("v<<<<")
    print(">>>>^")
else:
    if case_num <= 15:
        x_dim = random.randint(5, 20)
        y_dim = random.randint(5, 20)
    else:
        limit = min(case_num, 25)
        x_dim = random.randint(limit * 20, limit * 21)
        y_dim = random.randint(limit * 20, limit * 21)
    # def snake_pattern(x_dim, y_dim):
    print(x_dim, y_dim)
    board = dd(lambda : "#")
    y = 0
    while y < y_dim:
        cur_direction = 1
        for x in range(x_dim-1):
            board[y, x] = dirs[cur_direction]
        board[y, x_dim - 1] = "v"
        cur_direction = 3
        y += 1
        if y >= y_dim:
            break
        for x in range(x_dim-1, -1, -1):
            board[y, x] = dirs[cur_direction]
        board[y, 0] = "v"
        y += 1
    # random switches
    for _ in range(x_dim):
        change_x = random.randint(0, x_dim -1)
        change_y = random.randint(0, y_dim -1)
        board[change_y, change_x] = random.choice(list(dirs.values()))
        
    # place ring
    ring_dim = random.randint(min(x_dim, y_dim) // 2, min(x_dim, y_dim) - 1)
    corner_x = random.randint(0, x_dim - 1 - ring_dim) 
    corner_y = random.randint(0, y_dim - 1 - ring_dim) 
    for ring_x in range(ring_dim):
        board[corner_y, corner_x + ring_x] = ">"
    for ring_y in range(ring_dim):
        board[corner_y + ring_y, corner_x + ring_dim] = "v"
    for ring_x in reversed(range(1, ring_dim + 1)):
        board[corner_y+ ring_dim, corner_x + ring_x] = "<"
    for ring_y in reversed(range(1, ring_dim + 1)):
        board[corner_y + ring_y, corner_x] = "^"

        
    
    for y in range(y_dim):
        for x in range(x_dim):
            print(board[y,x], end='')               
        print()               
            

                

