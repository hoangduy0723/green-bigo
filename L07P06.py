def position(a): #return position in count list
    if ('A' <= a <= 'Z'):
        return (ord(a) - ord('A'))
    return (ord(a) - ord('a') + 26)
s = input()
count = [0] * 52 #initialize a list having 52 elements
for c in s:
    count[position(c)] += 1 #if char c appear in string, increment list 'count' at position c by 1
cnt = 0
for j in count:
    if j != 0: # if element in count list != 0, increment result 'cnt' by 1
        cnt += 1
print(cnt)