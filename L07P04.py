n = int(input())

for i in range(n):
    s = input()
    res = ""
    for j in range(len(s)):
        if (j == 0) or (s[j - 1] == ' '):
            if (s[j] >= 'a' and s[j] <= 'z'):
                res += chr(ord(s[j]) - 32)
            else:
                res += s[j]
        else:
            if (s[j] >= 'A' and s[j] <= 'Z'):
                res += chr(ord(s[j]) + 32)
            else:
                res += s[j]
    print(res)