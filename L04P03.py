def GCD(a, b):
    while(b != 0):
        t = b
        b = a % b
        a = t
    return a
x, y = map(int, input().split())
#print('{0} {1}'.format(int(x/GCD(x, y)), int(y/GCD(x, y))))
print(int(x / GCD(x, y)), int(y / GCD(x ,y)), end=' ')