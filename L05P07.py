n = int(input())
a = list(map(int, input().split()))
boys = 0
girls = 0
for i in a:
    if (i == 0):
        boys += 1
    if (i == 1):
        girls += 1
if (boys == girls):
    print("YES")
else:
    print("NO")