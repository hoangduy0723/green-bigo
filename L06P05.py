def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if (a % i == 0):
            return False
    return True

n = int(input())
a = []

for i in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)
product = 1
for i in range(n):
    if (isPrime(a[i][n - i - 1])):
        product *= a[i][n - i - 1]
print(product % 1000003)