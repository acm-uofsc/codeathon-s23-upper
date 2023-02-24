cases = int(input())
for i in range(cases):
    chain_length, moves = [int(x) for x in input().split()]
    chain = list(range(1, chain_length + 1))
    for move in range(moves):
        start, end, after = map(int, input().split())
        start_pos = chain.rindex(start)
        end_pos = chain.rindex(end)
        d = chain[start_pos:end_pos + 1]
        chain = chain[:start_pos] + chain[end_pos + 1:] 
        to_insert_after = chain.rindex(after)
        chain = chain[:to_insert_after + 1] + d + chain[to_insert_after + 1:]
    print(*chain[-5:])