n = int(input())
a = list(map(int, input().split()))
max_like = a[0]
for i in range (1, n):
    if (a[i] > max_like):
        max_like = a[i]
print(max_like)