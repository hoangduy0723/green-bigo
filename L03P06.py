flag = True
n = int(input())
for i in range (n):
    x = int(input())
    if (x % 2 != 0):
        flag = False
if (flag == True):
    print('YES')
else:
    print('NO')