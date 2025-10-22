n = [0,1,2,4,7]

for i in range(5, 11):
    n.append(n[i - 1] + n[i - 2] + n[i-3])


t = int(input())
tc = []
for i in range(t):
    tc.append(int(input()))

for i in tc:
    print(n[i])