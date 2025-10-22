# 도넛?
# 모든 정점을 돌아 특정 정점으로 돌아옴

# 막대? 종점이 있음(향하는 간선이 없는 점 존재)

# 8자 분기가 존재함

# 무작위 생성 정점 판별
# 해당 지점으로 향하는 간선 없음
# 막대면 .. 무조건 1간선
# 무작위 생성점이면 2간선 -> 그래프 수의 합은 2개 이상
# start > 2, end = 0 이면 시작점이다.

# 간선 판별 -> move
# 판별에서 갈 수 있는 간선 1개 -> move
# 갈 수 있는 간선 없음 -> 막대
# 갈 수 있는 간선 2개 -> 8자
def get_rand_vertex(edges):
    vs = [[0, 0] for _ in range(1000001)]
    for edge in edges:
        vs[edge[0]][0] += 1
        vs[edge[1]][1] += 1
        if vs[edge[0]][0] >= 3:
            return edge[0]
    
    for idx, v in enumerate(vs):
        if v[0] >= 2 and v[1] == 0:
            return idx

def graph(start, edge_map):
    cur = start
    while True:
        to_move = edge_map[cur]
        
        if not to_move:
            return 2 # 막대
        elif len(to_move) == 2:
            return 3
        elif len(to_move) == 1 and to_move[0] == start:
            return 1
        else:
            cur = to_move[0]
    
def solution(edges):
    edge_map = [[] for _ in range(1000001)]
    for edge in edges:
        edge_map[edge[0]].append(edge[1])
    
    start = get_rand_vertex(edges)

    ans = [start, 0, 0, 0]

    for v in edge_map[start]:
        g = graph(v, edge_map)
        if g == 1:
            ans[1] += 1
        elif g == 2:
            ans[2] += 1
        elif g == 3:
            ans[3] += 1
   
    return ans