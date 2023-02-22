import sys
import math
from collections import deque

class Node:
    def __init__(self, point, axis=0, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

def euclidean_distance(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))

def build_kdtree(points, depth=0):
    if not points:
        return None

    axis = depth % 2
    points.sort(key=lambda point: point[axis])

    mid = len(points) // 2
    left = build_kdtree(points[:mid], depth+1)
    right = build_kdtree(points[mid+1:], depth+1)

    return Node(points[mid], axis, left, right)

def find_closest_stores(root, customer_x, customer_y, k):
    closest_distances = [float('inf')] * k
    closest_stores = [[] for _ in range(k)]
    queue = deque([root])

    while queue:
        node = queue.popleft()
        x, y = node.point
        distance = euclidean_distance(customer_x, customer_y, x, y)

        for i in range(k):
            if distance < closest_distances[i]:
                closest_distances.insert(i, distance)
                closest_distances.pop()
                closest_stores.insert(i, [node.point])
                closest_stores.pop()
                break
            elif distance == closest_distances[i]:
                closest_stores[i].append(node.point)
                break

        if node.left and (customer_x - x) < closest_distances[-1]:
            queue.append(node.left)

        if node.right and (x - customer_x) < closest_distances[-1]:
            queue.append(node.right)

    return closest_stores

# read input from standard input
n, m = list(map(int, input().strip().split()))
stores =  input().strip().split()
stores = [tuple(map(int, point.split(','))) for point in stores]
customers =  input().strip().split()

# build k-d tree
root = build_kdtree(stores)

# find k closest stores
k = 1
for customer in customers:
    customer_x, customer_y = tuple(map(int, customer.split(',')))
    closest_stores = find_closest_stores(root, customer_x, customer_y, k)
    
    # print result
    for stores in closest_stores:
        for store in stores:
            print(store[0], store[1], sep=',')
