#Dòng đầu tiên chứa một số nguyên nn (1 \leq n \leq 100.000)(1≤n≤100.000) là số lượng nam châm.
#n dòng tiếp theo mỗi dòng chứa một cặp kí tự “01” nếu Mike đặt nam châm theo chiều (+)(-) hoặc “10” nếu theo chiều ngược lại.
n = int(input())
s = ""
cnt = 1
for _ in range(n):
    str = input()
    s += str
for i in range(len(s) - 1):
    if (s[i] == s[i + 1]):
        cnt += 1
print(cnt)