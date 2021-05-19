def max_OnDirection(a, n, row, col, x, y):
    i = row
    j = col
    while (0 <= i < n and 0 <= j < n):
        if (a[i][j] > a[row][col]):
            return False
        i += x
        j += y
    return True

def isQueen(a, n, row, col):
    for j in range(n):
        if (a[row][j] > a[row][col]):
            return False
    for i in range(n):
        if (a[i][col] > a[row][col]):
            return False
    dir1 = max_OnDirection(a, n, row, col, -1, -1)
    dir2 = max_OnDirection(a, n, row, col, 1, 1)
    dir3 = max_OnDirection(a, n, row, col, 1, -1)
    dir4 = max_OnDirection(a, n, row, col, -1, 1)
    return (dir1 and dir2 and dir3 and dir4)

n = int(input())
a = []

for i in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)
cnt = 0
for i in range(n):
    for j in range(n):
        if (isQueen(a, n, i, j)):
            cnt += 1
print(cnt)