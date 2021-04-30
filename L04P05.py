def maxDigit(a):
    max_digit = -1
    temp = a
    while (temp > 0):
        b = temp % 10
        if (b > max_digit):
            max_digit = b
        temp = temp // 10
    return max_digit
n = int(input())
print(maxDigit(n))