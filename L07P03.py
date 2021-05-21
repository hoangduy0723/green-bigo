s = input()
res = ""
needSpace = False
for i in s:
    if (i == ' ' and len(res) > 0): #len(res) > 0 để không chèn khoảng trắng ở đầu
        needSpace = True #cập nhật needSpace = True
    if (i != ' '):
        if (needSpace):
            res += ' ' #thêm khoảng trắng trước
            res += i #rồi mới chèn ký tự vào res
            needSpace = False #gán lại needSapce = False
        else:
            res += i #chèn ký tự vào res
print(res)