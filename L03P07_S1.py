#Ta thấy rằng với một hàng rào hình vuông có độ dài cạnh là n, thì hàng 1 và hàng n sẽ gồm n dấu * được viết liên tục. Trong khi đó trên mỗi hàng từ hàng 2 đến hàng n – 1, chỉ gồm một dấu * ở vị trí đầu và một dấu * ở vị trí cuối, còn lại giữa 2 ký tự * đó hoàn toàn không có gì.
#Như vậy, ta sẽ in ra được hàng rào bằng cách như sau:
#Ta in ra hàng rào thứ 1, bằng cách duyệt một vòng lặp lặp lại n lần, mỗi lần in ra dấu *, và phải nhớ chuyển xuống dòng dưới để in tiếp.
#Ta lặp lại n – 2 lần, tương ứng với việc vẽ hàng rào trên các hàng từ 2 đến n – 1, với mỗi lần lặp, ta in ra dấu * đầu tiên. Tiếp theo là ta lại lặp lại n – 2 lần và in tiếp ra màn hình ký tự khoảng trắng. Cuối cùng ta in ra thêm một dấu * và chuyển tiếp xuống dòng dưới.
#Cuối cùng, ta duyệt một vòng lặp lặp n lần, mỗi lần in ra dấu * nhằm mục đích in ra hàng rào ở hàng cuối cùng.
n = int(input())
for i in range (n):
    print('*', end='')
print()
for i in range(1, n - 1):
    print('*', end='')
    for j in range (1, n - 1):
        print(' ', end='')
    print('*')
for i in range(n):
    print('*', end='')