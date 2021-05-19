m, n = map(int, input().split())
a = []

for i in range (m):
    temp = list(map(int, input().split()))
    a.append(temp)
for j in range (n):
    flag = True
    for i in range (m):
        if (a[i][j] >= 0):
            flag = False
    if (flag == True):
        print(j, end=" ")