#Cho bạn một chuỗi là tên của một bài hát. Để dễ tìm kiếm, đề bài yêu cầu in ra tên viết tắt chữ cái đầu của bài hát đó dưới dạng chữ hoa.
s = input()
s = s.upper()
res = ""
for i in range(len(s)):
    if (i == 0) or (s[i - 1] == ' '):
        res += s[i]
print(res)