def numberOfDigits(a):
    digit = 0
    temp = a
    while (temp > 0):
        b = temp % 10
        digit += 1
        temp = temp // 10
    return digit
n = int(input())
print(numberOfDigits(n))