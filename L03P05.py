flag = True
min_flower = 0
while (1 < 2):
    height = int(input())
    if (height == 0):
        break
    if (height < min_flower):
        flag = False
    min_flower = height
if (flag == True):
    print('YES')
else:
    print('NO')