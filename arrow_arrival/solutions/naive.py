from collections import defaultdict
import sys
x_dim, y_dim = map(int, input().split())
board = [input() for _ in range(y_dim)]

assert all(len(line) == x_dim for line in board)

arrow_to_direction = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

sys.setrecursionlimit(1000000)

def dfs(x, y, path_length=0, cur_path_seen=None):
    '''returns how many tiles were reachable from this (x, y), and if the path hit itself'''
    if cur_path_seen is None:
        cur_path_seen = {}
    cur_pos = (y, x)
    if x not in range(x_dim) or y not in range(y_dim):
        return path_length
    if cur_pos in cur_path_seen:
        return path_length
    cur_path_seen[cur_pos] = path_length
    dy, dx = arrow_to_direction[board[y][x]]
    x += dx
    y += dy
    return dfs(x, y, path_length + 1, cur_path_seen)

lengths = defaultdict(int)
best = -1
for y in range(y_dim):    
    for x in range(x_dim):    
        best = max(best, dfs(x, y))
print(best)
