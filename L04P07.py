def reverseNum(a):
    rev = 0
    temp = a
    while (temp > 0):
        mod = temp % 10
        rev = 10 * rev + mod
        temp = temp // 10
    if (rev == a):
        return True
    else:
        return False
n = int(input())
if (reverseNum(n)):
    print('YES')
else:
    print('NO')