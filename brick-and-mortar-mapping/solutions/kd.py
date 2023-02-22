import math

class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def euclidean_distance(p1, p2):
    return math.dist((x1, y1), (x2, y2))


def build_kd_tree(points, depth=0):
    n = len(points)
    if n <= 0:
        return None

    axis = depth % 2
    points = sorted(points, key=lambda x: x[axis])
    median = n // 2
    return Node(
        points[median],
        build_kd_tree(points[:median], depth + 1),
        build_kd_tree(points[median + 1:], depth + 1)
    )


def search_kd_tree(root, point, depth=0):
    if root is None:
        return None, float('inf')

    axis = depth % 2
    next_branch = root.left if point[axis] < root.point[axis] else root.right
    opposite_branch = root.right if next_branch is root.left else root.left

    best, best_distance = search_kd_tree(next_branch, point, depth + 1)

    if best is None or (point[axis] - root.point[axis]) ** 2 < best_distance:
        candidate, candidate_distance = search_kd_tree(opposite_branch, point, depth + 1)
        if candidate is not None and candidate_distance < best_distance:
            best, best_distance = candidate, candidate_distance

    if (point[axis] - root.point[axis]) ** 2 < best_distance:
        current_distance = sum((point[i] - root.point[i]) ** 2 for i in range(2))
        if current_distance < best_distance:
            best, best_distance = root.point, current_distance

    return best, best_distance
    
n, m = list(map(int, input().strip().split()))
stores =  input().strip().split()
stores = [tuple(map(int, point.split(','))) for point in stores]
customers =  input().strip().split()
root = build_kd_tree(stores)
for customer in customers:
    point = tuple(map(int, customer.split(',')))
    closest_store, _ = search_kd_tree(root, point)
    print(*closest_store, sep=',')