def dfs(sum_target, depth, numbers, target):
    if depth == len(numbers):
        if sum_target == target:
            return 1
        else:
            return 0
        
    return dfs(sum_target + numbers[depth], depth + 1, numbers, target) + dfs(sum_target - numbers[depth], depth + 1, numbers, target)
    
def solution(numbers, target):
    return dfs(0, 0, numbers, target)