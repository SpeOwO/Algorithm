from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []
city = []
for i in range(n):
    temp = list(map(int, input().split()))
    for idx, j in enumerate(temp):
        if j == 1:
            house.append([i, idx])
        elif j == 2:
            chicken.append([i, idx])
    city.append(temp)

ans = float("inf")

combi = combinations(chicken, m)

for com in combi:
    total_dist = 0
    for h in house:
        dist = float("inf")
        for c in com:
            dist = min(dist, (abs(h[0] - c[0]) + abs(h[1] - c[1])))
        total_dist += dist

    ans = min(ans, total_dist)

print(ans)