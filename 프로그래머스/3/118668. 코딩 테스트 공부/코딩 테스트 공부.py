import math
INF = math.inf
def solution(alp, cop, problems):
    answer = INF
    max_alp, max_cop = 0, 0
    for a in problems:
        max_alp = max(max_alp, a[0])
        max_cop = max(max_cop, a[1])
    
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if a < max_alp:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
            if c < max_cop:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= a and cop_req <= c:
                    na, nc = min(a+alp_rwd, max_alp), min(c+cop_rwd, max_cop)
                    dp[na][nc] = min(dp[na][nc], dp[a][c] + cost)
    
    return dp[max_alp][max_cop]