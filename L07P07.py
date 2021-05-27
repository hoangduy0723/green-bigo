s = input()
res = ""
for i in range(len(s)):
    if (i >= 2 and s[i - 2] == '.' and s[i - 1] == ' ') and ('a' <= s[i] <= 'z'):
        res += chr(ord(s[i]) - 32)
    else:
        res += s[i]
print(res)