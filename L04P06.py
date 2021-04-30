def isPrime(a):
    if (a < 2):
        return False
    elif (a == 2):
        return True
    else:
        for i in range (2, int(n ** 0.5 + 1)):
            if (a % i == 0):
                return False
    return True
def primeNumbersNearest(a):
    n1 = n2 = a
    while (1 < 2):
        if (isPrime(n1)):
            ans = n1
            break
        else:
            n1 -= 1
        if (isPrime(n2)):
            ans = n2
            break
        else:
            n2 += 1
    return ans
n = int(input())
print(primeNumbersNearest(n))