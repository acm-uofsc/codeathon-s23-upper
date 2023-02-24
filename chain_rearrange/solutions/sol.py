import sys

class Node:
    def __init__(self, val=None, prev:'Node'=None, next:'Node'=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

def print_linked_list(head):
    # return
    cur = head
    while cur.next is not None:
        print(cur.val, end=' ', file=sys.stderr)
        cur = cur.next
    print(file=sys.stderr)

def rearrange(start, end, node_to_insert_after, value_to_node):
    start = value_to_node[start]
    end = value_to_node[end]
    node_to_insert_after = value_to_node[node_to_insert_after]

    #remove the section by joining the two ends together
    before_start = start.prev
    after_end = end.next
    before_start.next = after_end
    after_end.prev = before_start
    
    # 11
    temp_after = node_to_insert_after.next
    # after following line, 11 points to 
    node_to_insert_after.next = start
    start.prev = node_to_insert_after
    
    end.next = temp_after
    temp_after.prev = end

def setup_list(link_count):
    '''returns the head, the spot after the last node, and value_to_node'''
    head = Node(-1234)
    cur = head
    value_to_node = {}
    for i in range(1, link_count + 1):
        cur.next = Node(val=i, prev=cur)
        value_to_node[i] = cur.next
        cur = cur.next
    cur.next = Node(-1, prev=cur)
    place_holder_last_node = cur.next
    return head, value_to_node, place_holder_last_node


def solve():
    link_count, instructions = map(int, input().split())
    head, value_to_node, dummy_end = setup_list(link_count)
    print_linked_list(head.next)
    for line in range(instructions):
        start, end, node_to_insert_after = map(int, input().split())
        rearrange(start, end, node_to_insert_after, value_to_node)
        print_linked_list(head.next)
    last5 = []
    end = dummy_end
    for i in range(5):
        end = end.prev
        last5.append(end.val)
    # cur = head
    # while cur is not None:
    #     last5.append(cur.val)
    #     cur = cur.next
        
    # bottom = spot_after_last.prev
    # for i in range(5):
    #     last5.append(bottom.val)
    #     bottom = bottom.prev
    print(*last5[::-1])

if __name__ == '__main__':
    cases = int(input())
    for t in range(cases):
        solve()
    

