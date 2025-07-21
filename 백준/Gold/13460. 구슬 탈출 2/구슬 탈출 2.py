import sys
from collections import deque

def reverse(state):
    reversed_state = []
    for line in state:
        reversed_state.append(line[::-1])
    return reversed_state

def transpose(state):
    transposed_state = [list(x) for x in zip(*state)]
    return transposed_state

def right(state):
    new_state = []
    rolling = deque()
    for line in state:
        if 'R' not in line and 'B' not in line:
            new_state.append(line[:])
            continue

        new_line = []
        for idx, element in enumerate(line):
            if len(rolling) > 0 and element == '#':
                new_line.append('#')
                new_line[idx-1] = rolling.pop()
                if len(rolling) > 0:
                    new_line[idx-2] = rolling.pop()

            elif len(rolling) > 0 and element == 'O':
                if len(rolling) == 2:
                    return False
                else:
                    marble = rolling.pop()
                    if marble == 'R':
                        return True
                    elif marble == 'B':
                        return False

            elif element == 'R' or element == 'B':
                rolling.append(element)
                new_line.append('.')

            else:
                new_line.append(element)

        new_state.append(new_line)

    return new_state

def left(state):
    new_state = reverse(state)
    new_state = right(new_state)
    if new_state == True:
        return True
    elif new_state == False:
        return False
    else:
        new_state = reverse(new_state)
    return new_state

def up(state):
    transposed_state = transpose(state)
    new_state = left(transposed_state)
    if new_state == True:
        return True
    elif new_state == False:
        return False
    else:
        new_state = transpose(new_state)
        return new_state

def down(state):
    transposed_state = transpose(state)
    new_state = right(transposed_state)
    if new_state == True:
        return True
    elif new_state == False:
        return False
    else:
        new_state = transpose(new_state)
        return new_state


def bfs(state):
    depth_q = deque()
    state_q = deque()

    depth_q.append(1)
    state_q.append(state)

    while len(depth_q) > 0:
        depth = depth_q.popleft()
        if depth >= 11:
            break
        state = state_q.popleft()

        new_state = left(state)
        if new_state == True:
            return depth
        elif new_state == False or state == new_state:
            pass
        else:
            depth_q.append(depth+1)
            state_q.append(new_state)

        new_state = right(state)
        if new_state == True:
            return depth
        elif new_state == False or state == new_state:
            pass
        else:
            depth_q.append(depth+1)
            state_q.append(new_state)

        new_state = up(state)
        if new_state == True:
            return depth
        elif new_state == False or state == new_state:
            pass
        else:
            depth_q.append(depth+1)
            state_q.append(new_state)

        new_state = down(state)
        if new_state == True:
            return depth
        elif new_state == False or state == new_state:
            pass
        else:
            depth_q.append(depth+1)
            state_q.append(new_state)

    return -1

# get input
n, m = map(int, input().split())

state = []

for i in range(n):
    state.append(list(sys.stdin.readline().rstrip()))

print(bfs(state))