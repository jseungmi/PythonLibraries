#Number - 정수형, 실수형
a = 3
print(type(a))
b = 3.3
print(type(b))
a = float(a)
print(type(a))
c = 3.0
print(type(c))

#Number - 2진수, 8진수, 16진수
k = 0b11
i = 0o77
j = 0xA

print("2진수,11:",int(k), "8진수,77:", int(i), "16진수,A:", int(j))

#Boolean
t, t1 = True, 1 
f, f1 = False, 0

print(t == t1, f == f1)
