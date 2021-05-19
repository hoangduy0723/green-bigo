m, n = map(int, input().split())
a = []

for i in range(m):
    temp = list(map(int, input().split()))
    a.append(temp)
max_even = 0
index = -1
for i in range(m):
    cnt = 0
    for j in range(n):
        if (a[i][j] % 2 == 0):
            cnt += 1
    if (cnt > max_even):
        max_even = cnt
        index = i
print(index)