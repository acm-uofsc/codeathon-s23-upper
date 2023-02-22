import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_closest_store(customer_x, customer_y, stores):
    closest_distance = float('inf')
    closest_store = None
    for store_x, store_y in stores:
        distance = euclidean_distance(customer_x, customer_y, store_x, store_y)
        if distance < closest_distance:
            closest_distance = distance
            closest_store = (store_x, store_y)
    return closest_store

n, m = list(map(int, input().strip().split()))
stores =  input().strip().split()
stores = [tuple(map(int, point.split(','))) for point in stores]
customers =  input().strip().split()

for customer in customers:
    customer = tuple(map(int, customer.split(',')))
    closest_store = find_closest_store(customer[0], customer[1], stores)
    print(*closest_store, sep=',')