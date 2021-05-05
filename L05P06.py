n = int(input())
h = list(map(int, input().split()))
energy = 0
min_height = h[0]
for i in range(1, n):
    if (h[i] < min_height):
        min_height = h[i]
for i in h:
    energy += i - min_height
print(energy)