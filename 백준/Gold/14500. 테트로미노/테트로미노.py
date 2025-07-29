n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False] * m for _ in range(n)]

maximum = 0

def dfs(x, y, sum_tetro, cnt):
    global maximum

    if cnt == 4:
        maximum = max(maximum, sum_tetro)
        return

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or visited[new_y][new_x] == True:
            continue
        visited[new_y][new_x] = True
        dfs(new_x, new_y, sum_tetro + board[new_y][new_x], cnt + 1)
        visited[new_y][new_x] = False

def t(x, y):
    global maximum

    box = []
    l = 0
    for i in range(4):
        new_x = dx[i] + x
        new_y = dy[i] + y
        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
            continue
        box.append(board[new_y][new_x])
        l += 1
    if l == 2:
        return
    if l == 3:
        maximum = max(maximum, board[y][x] + sum(box))
    elif l == 4:
        box.sort(reverse=True)
        box.pop()
        maximum = max(maximum, board[y][x] + sum(box))

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, board[i][j], 1)
        t(j, i)
        visited[i][j] = False

print(maximum)