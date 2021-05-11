n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
id = 0
for i in range(1, n):
    if (a[i] > a[id] or (a[i] == a[id] and b[i] > b[id])):
        id = i
print(id + 1)