def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if (a % i == 0):
            return False
    return True
a = []
m, n = map(int, input().split())
for i in range (m):
    temp = list(map(int, input().split()))
    a.append(temp)
count = 0
for j in range(n):
    if (isPrime(a[0][j])):
        count += 1
    if(isPrime(a[m - 1][j])):
        count += 1
for i in range(1, m - 1):
    if (isPrime(a[i][0])):
        count += 1
    if (isPrime(a[i][n - 1])):
        count += 1
print(count)