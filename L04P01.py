def isPrime(a):
    if (a < 2):
        return False
    elif (a == 2):
        return True
    else:
        for i in range (2, int(a**0.5 + 1)):
            if (a % i == 0):
                return False
    return True
def sumOfPrime(x):
    sum = 0;
    for i in range(2, x):
        if (isPrime(i)):
            sum += i
    return sum
n = int(input())
print(sumOfPrime(n))