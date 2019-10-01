#loop, for문
scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)

word = "hi"
for _ in word:
    print(_)

codes = {"a":97, "b":98, "c":99}
for _ in codes:
    print(_)

for _ in codes.values():
    print(_)

for _ in codes.items():
    print(_)

#for _ in 20:
#    print(_)

#많이 하는 for문
a = []
for _ in range(1,10):
    a.append(_)

print(a)

#Conditional, if문

point = int(input("점수를 입력하세요"))

if point >= 90:
    print("A")
elif 80 <= point < 90:
    print("B")
elif 70 <= point < 80:
    print("C")
elif 60 <= point <70:
    print("D")
elif point <60:
    print("F")


#loop, while문


