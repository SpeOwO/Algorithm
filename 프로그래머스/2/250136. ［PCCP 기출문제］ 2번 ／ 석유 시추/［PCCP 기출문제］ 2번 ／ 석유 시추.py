# bfs
from collections import deque
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(visited, land, size_arr, y, x, n, m):
    q = deque()
    q.append((y, x))
    size = 0
    av = set()
    av.add(x)
    
    while q:
        y, x = q.popleft()
        av.add(x)
        size += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            elif land[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny, nx))

    for av_x in av:
        size_arr[av_x] += size

def solution(land):
    m = len(land[0])
    n = len(land)
    answer = 0
    visited = [[0 for i in range(m)] for j in range(n)]
    size_arr = [0 for i in range(m)]
    for y in range(n):
        for x in range(m):
            if land[y][x] == 0 or visited[y][x] == 1:
                visited[y][x] = 1
                continue
            else:
                visited[y][x] = 1
                bfs(visited, land, size_arr, y, x, n, m)
    print(size_arr)
    return max(size_arr)