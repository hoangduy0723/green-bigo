def sumOfSquares(a):
    sum = 0
    for i in range(1, a + 1):
        sum += i * i
    return sum
n = int(input())
print(sumOfSquares(n))