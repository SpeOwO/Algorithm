# dfs 완전 탐색
def is_changeable(begin, target):
    cnt = 0
    for i in range(len(begin)):
        if begin[i] == target[i]:
            cnt += 1
    if cnt == len(begin) - 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 51
    visited = [False] * len(words)
    def dfs(depth, cur):
        nonlocal answer
        if cur == target:
            answer = min(answer, depth)
        for idx, w in enumerate(words):
            if is_changeable(cur, w) and not visited[idx]:
                visited[idx] = True
                dfs(depth + 1, w)
                visited[idx] = False
        
    dfs(0, begin)
    return answer if answer != 51 else 0