m, n = map(int, input().split())
a, b, p = map(int, input().split())

A = [[0 for i in range(n)] for j in range(m)] #create matrix m rows and n cols
A[0][0] = a
A[0][1] = b
for i in range(m):
    if (i == 0):
        for j in range(2, n):
            c = (a + b) % p
            a = b
            b = c
            A[i][j] = c
    else:
        for j in range(n):
            c = (a + b) % p
            a = b
            b = c
            A[i][j] = c
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()