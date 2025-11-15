from collections import deque

# 세팅
n, m = map(int, input().split())
# 그래프 연결하기
graph = [[] for i in range(n + 1)]
degree = [0 for i in range(n + 1)]
queue = deque()
answer = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

# 위상 정렬하기
# 1. 진입 차수 0인 것 큐에 넣기

for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    answer.append(cur)
    for i in graph[cur]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

for i in answer:
    print(i, end=" ")