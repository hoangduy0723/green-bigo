#Cho một câu gồm nhiều từ cách nhau bởi khoảng trắng, viết chương trình đảo ngược thứ tự các từ trong câu lại.
s = input()
words = []
word = ""
for i in s:
    if (i == ' '):
        words.append(word)
        word = ""
    else:
        word += i
if (len(word)) > 0:
    words.append(word)
res = ""
for i in range(len(words) - 1, -1, -1):
    res += words[i] + ' '
print(res)