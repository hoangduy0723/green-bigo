s = input()
cnt = 0
for c in s:
    if (ord(c) >= 48 and ord(c) <= 57):
    #if ('0' <= c <= '9'):
        cnt += 1
print(cnt)