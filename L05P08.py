n = int(input())
a = list(map(int, input().split()))

def inArray(k, arr):
    for i in arr:
        if (k == i):
            return True
    return False

ans = 1
while True:
    if (inArray(ans, a)):
        ans += 1
        continue
    else:
        print(ans)
        break