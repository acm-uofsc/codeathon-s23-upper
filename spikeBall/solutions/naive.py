from math import dist

def calc(center1, center2, spikes1, spikes2):
    center_diff = dist(center1, center2)
    if not spikes1:
        spikes1 = [center1]
    if not spikes2:
        spikes2 = [center2]

    for spike in spikes1:
        for spike2 in spikes2:
            longest1 = dist(center1, spike)
            longest2 = dist(center2, spike2)
            if longest1 + longest2 >= center_diff:
                return "true"
    return "false"


cases = int(input())
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
    print(calc(center1, center2, spikes1, spikes2))