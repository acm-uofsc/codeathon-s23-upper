import sys
from math import dist

# def dist(p, q):
#     return (sum((px - qx) ** 2.0 for px, qx in zip(p, q))) ** .5


def main():
    cases = int(input())
    trues = 0
    for t in range(cases):
        x1, y1, x2, y2 = map(int, input().split())
        center1 = (x1, y1)
        center2 = (x2, y2)
        n_spike_count1 = int(input())
        spikes1 = [tuple(int(x) for x in input().split()) for _ in range(n_spike_count1)]
        assert len(spikes1) == n_spike_count1
        m_spike_count2 = int(input())
        spikes2 = [tuple(int(x) for x in input().split()) for _ in range(m_spike_count2)]
        assert len(spikes2) == m_spike_count2


        if not spikes1:
            longest1 = 0
        else:
            # longest1 = max(dist_no_sqrt(center1, spike_end) for spike_end in spikes1)
            longest1 = max(dist(center1, spike_end) for spike_end in spikes1)
        if not spikes2:
            longest2 = 0
        else:
            # longest2 = max(dist_no_sqrt(center2, spike_end) for spike_end in spikes2)
            longest2 = max(dist(center2, spike_end) for spike_end in spikes2)
        
        center_diff = dist(center1, center2)
        # print(longest1, longest2, center_diff, file=sys.stderr)
        # print(longest1_euc, longest2_euc, dist(center1, center2), file=sys.stderr)
        if longest1 + longest2 >= center_diff:
            trues += 1
            print("true")
        else:
            print("false")
    # assert trues != cases
    # assert trues != 0


if __name__ == '__main__':
    main()