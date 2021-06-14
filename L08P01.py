n = int(input())
vnd = 0
if n <= 1:
    vnd = 15000
elif n <= 5:
    vnd = 15000 + (n - 1) * 13500
else:
    vnd = 15000 + 4 * 13500 + (n - 5) * 11000
if (n >= 12):
    vnd = vnd * 0.9
print(int(vnd))