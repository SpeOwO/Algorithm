# bfs
from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((0, 0))
    visited = [([False] * m) for i in range(n)]
    visited[0][0] = True
    while q:
        y, x = q.popleft()
        print(y, x)
        if y == n - 1 and x == m - 1:
            return maps[n - 1][m - 1]
        for i in range(0, 4):        
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if visited[ny][nx] or maps[ny][nx] == 0:
                continue
            else:
                visited[ny][nx] = True
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))  
    return -1