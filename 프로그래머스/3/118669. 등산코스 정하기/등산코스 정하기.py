from collections import defaultdict
import heapq
INF = 10000001

def solution(n, paths, gates, summits):
    answer = []
    graph = defaultdict(list)
    set_summits = set(summits)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    pq = [(0, g) for g in gates]
    d = [INF] * (n + 1)
    while pq:
        w, cur_v = heapq.heappop(pq)
        if d[cur_v] > w:
            d[cur_v] = w
        else:
            continue
        for nw, ni in graph[cur_v]:
            cost = max(nw, w)
            if d[ni] <= cost:
                continue
            if ni in set_summits:
                d[ni] = min(d[ni], cost)
                continue
            heapq.heappush(pq, (cost, ni))
    
    answer = [0, INF]
    for s in sorted(summits):
        if d[s] < answer[1]:
            answer = [s, d[s]]
    return answer