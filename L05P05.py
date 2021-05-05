def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if (a % i == 0):
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    if (isPrime(i)):
        count += 1
print(count)