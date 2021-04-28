bag1, bag2, bag3, bag4 = map(int, input().split())
max_candy = bag1
if (bag2 > max_candy):
    max_candy = bag2
if (bag3 > max_candy):
    max_candy = bag3
if (bag4 > max_candy):
    max_candy = bag4
print(max_candy)
