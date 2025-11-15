def union(i, j, nodes):
    if nodes[i] < nodes[j]:
        target = nodes[j]
        for k in range(len(nodes)):
            if nodes[k] == target:
                nodes[k] = nodes[i]
    else:
        target = nodes[i]
        for k in range(len(nodes)):
            if nodes[k] == target:
                nodes[k] = nodes[j]
    
def solution(n, computers):
    answer = 0
    nodes = [i for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if computers[i][j] == 1:
                union(i, j, nodes)

    return len(set(nodes))