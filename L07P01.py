s = input()
lch = ['B', 'I', 'G', 'O', 'b', 'i', 'g', 'o']
flag = False
for c in s:
    if c in lch:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')