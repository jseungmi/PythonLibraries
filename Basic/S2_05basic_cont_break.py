a = 0
while True:
    a += 1
    print(a)
    # if a == 10:
    #     break


x = 0
while x < 10:
    x = x + 1
    if x < 3:
        break # while 구문을 멈춤.

print(x)


y = 0
while y < 10:
    y = y + 1 #line순서 바꾸기!!!
    if y < 5:
        continue # while 구문을 처음으로 이동하여 반복문 계속

print(y)