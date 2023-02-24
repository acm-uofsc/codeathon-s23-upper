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

ever_seen = defaultdict(int)
sys.setrecursionlimit(1000000)


def dfs(x, y, path_length=0, cur_path_seen=None):
    '''returns how many tiles were reachable from this (x, y)'''
    if cur_path_seen is None:
        cur_path_seen = {}
    cur_pos = (y, x)
    if x not in range(x_dim) or y not in range(y_dim):
        return path_length
    if cur_pos in cur_path_seen:
        for spot in cur_path_seen:
            if cur_path_seen[spot] >= cur_path_seen[cur_pos]:
                ever_seen[spot] = path_length - cur_path_seen[cur_pos]
        return path_length
    cur_path_seen[cur_pos] = path_length
    if cur_pos in ever_seen:
        return path_length + ever_seen[cur_pos]
    dy, dx = arrow_to_direction[board[y][x]]
    x += dx
    y += dy
    total_path_length = dfs(x, y, path_length + 1, cur_path_seen)
    ever_seen[cur_pos] = max(ever_seen[cur_pos], total_path_length - path_length)
    return total_path_length

for y in range(y_dim):    
    for x in range(x_dim):    
        dfs(x, y)
for y in range(y_dim):
    for x in range(x_dim):
        print(ever_seen[y, x], end='\t')
    print()
print(max(ever_seen.values()))

