def position(a):
    if ('A' <= a <= 'Z'):
        return (ord(a) - ord('A'))
    return (ord(a) - ord('a'))

def getMinOccurChar(s):
    count = [0] * 26
    for c in s:
        count[position(c)] += 1
    min_temp = 1001
    res = ''
    for i in range(len(count)):
        if (count[i] != 0 and count[i] < min_temp):
            min_temp = count[i]
            res = chr(i + ord('A'))
    return res

n = int(input())
for i in range(n):
    str = input()
    print(getMinOccurChar(str))