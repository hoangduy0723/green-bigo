def maxRow(a, m, n, row, col):
    for j in range(n): #max_row
        if (a[row][j] > a[row][col]):
            return False
    return True

def minCol(a, m, n, row, col):
    for i in range(m): #min_col
        if (a[i][col] < a[row][col]):
            return False
    return True

def isHorseSaddle(a, m, n, row, col):
    if (minCol(a, m, n, row, col) and maxRow(a, m, n, row, col)):
        return True
    return False

m, n = map(int, input().split())
a = []

for i in range(m):
    temp = list(map(int, input().split()))
    a.append(temp)
cnt = 0
for i in range(m):
    for j in range(n):
        if (isHorseSaddle(a, m, n, i, j)):
            cnt += 1
print(cnt)