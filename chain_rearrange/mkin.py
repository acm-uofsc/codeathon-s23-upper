#!/usr/local/bin/python3
from solutions.sol import Node, setup_list, rearrange

import random
case_num = int(input())
random.seed(case_num)
# 0 and 1 are the sample cases
if case_num == 0:
    # 1 2 3 4 5 6 7 8 9 10 11 12
# 9 1 2 3 4 5 6 7 8 10 11 12
# 5 6 7 8 9 1 2 3 4 10 11 12
# 10 11 12 5 6 7 8 9 1 2 3 4
    print(1)
    print(12, 3)
    print(1, 8, 9)
    print(9, 4, 8)
    print(5, 4, 12)

elif case_num == 1:
    # 1 2 3 4 5 6 7 8 9 10
    # 1 2 3 7 8 9 10 4 5 6
    # 1 2 7 8 9 10 3 4 5 6
    print(2)
    print(10, 2)
    print(4, 6, 10)
    print(7, 10, 2)

    # 1 2 3 4 5 6 7
    # 7 1 2 3 4 5 6 
    # 3 7 1 2 4 5 6 
    # 3 1 2 4 5 7 6  
    print(7, 3)
    print(1, 6, 7)
    print(7, 2, 3)
    print(1, 5, 3)
else:
    # output what should be read in as input by
    # contestant code
    hard_cut_off = 15
    case_count = random.randint(3, 5)
    if case_num > hard_cut_off:
        case_count = 2
    print(case_count)
    move_limit = 200_000
    for c in range(case_count):
        if case_num < 10:
            n = random.randint(150, 300)
            moves = random.randint(30, 40)
        elif case_num < hard_cut_off:
            n = random.randint(1000, 1200)
            moves = random.randint(1000, 1100)
        else:
            n = random.randint(100_000, 110_000)
            moves = random.randint(100_000, 102_000)
        head, value_to_node, place_holder_last_node = setup_list(n)
        
        print(n, moves)

        for move_number in range(moves):
            chain_length_after_start = random.randint(1, 5)
            # start_pos = random.randint(1, n-4)
            # cur_start_node = value_to_node[start_pos]
            start_pos_from_end = random.randint(2, min(10, n//2))
            cur_start_node = place_holder_last_node
            for i in range(start_pos_from_end):
                cur_start_node = cur_start_node.prev
            # while cur_start_node.next.next is None or cur_start_node.next.next.next is None:

            # if move_number % 2 == 0:
            #     end = cur_start_node
            #     for i in range(chain_length_after_start):
            #         if end.next.next.next is not None:
            #             end = end.next
            # else:
            end = cur_start_node
            for i in range(move_number % 5 + 1):
                if end.next.next is None:
                    break
                end = end.next

            # options_to_insert_after = []
            # temp_left = cur_start_node
            # temp_right = end
            # insert_after_distance_away = random.randint(2, n//3 + 1)
            # for i in range(insert_after_distance_away):
            #     if temp_left.prev.prev is not None:
            #         temp_left = temp_left.prev
            #         done = True
            #     if temp_right.next.next is not None:
            #         temp_right = temp_right.next
            #         done = True
            #     if done:
            #         break
            # if temp_left.prev.prev is not None:
            #     options_to_insert_after.append(temp_left)
            # if temp_right.next.next is not None:
            #     options_to_insert_after.append(temp_right)
            # if not options_to_insert_after:
            #     options_to_insert_after = [temp_left]
            # insert_after = random.choice(options_to_insert_after)
            insert_after = head
            distance_after_start_to_insert = random.randint(1, 6)
            for i in range(distance_after_start_to_insert):
                if insert_after.next == cur_start_node:
                    break
                insert_after = insert_after.next

            rearrange(cur_start_node.val, end.val, insert_after.val, value_to_node)
            testing_start = value_to_node[cur_start_node.val]
            while testing_start.val != end.val:
                assert testing_start.val != insert_after.val
                testing_start = testing_start.next
            print(cur_start_node.val, end.val, insert_after.val)

    


    
    # end_node = cur_start_node
    # for i in range(chain_length):
    #     end_node = end_node.next
    # should_choose_before = random.randint(0,1)
    # if should_choose_before:
        # to_insert_after =  



    # after = random.randint(end + 1, n)

