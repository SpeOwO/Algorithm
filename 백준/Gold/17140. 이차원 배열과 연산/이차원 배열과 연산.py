def sort_row(arr):
    new_array = []
    for line in arr:
        new_line = []
        count_arr = [[i, 0] for i in range(0, 101)]
        for ele in line:
            if ele == 0:
                continue
            count_arr[ele][1] += 1
        count_arr = sorted(count_arr, key = lambda x : (x[1], x[0]))
        for e in count_arr:
            if e[1] == 0:
                continue
            else:
                new_line.append(e[0])
                new_line.append(e[1])
        new_array.append(new_line)

    # 0 스패밍
    max_len = 0
    for line in new_array:
        max_len = max(max_len, len(line))

    for i in range(len(new_array)):
        while True:
            if len(new_array[i]) == max_len:
                break
            else:
                new_array[i].append(0)

    return new_array

def sort_col(arr):
    transposed_arr = transpose(arr)
    transposed_arr = transpose(sort_row(transposed_arr))
    return transposed_arr

def transpose(arr):
    transposed_arr = []
    for line in zip(*arr):
        transposed_arr.append(line)
    return transposed_arr

r, c, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]

timer = 0

while True:
    if r-1 < len(A) and c-1 < len(A[0]):
        if A[r-1][c-1] == k:
            break

    if len(A) >= len(A[0]):
        A = sort_row(A)
    else:
        A = sort_col(A)

    timer += 1
    if timer == 101:
        timer = -1
        break

print(timer)
