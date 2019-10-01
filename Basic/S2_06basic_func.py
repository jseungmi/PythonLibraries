#function basic
def hello():
    return "hi"

a = print(hello())

#function parameter
def area(r):
    return 3.1415 * r**2

b = area(5)
print(b)


def exponential(a,b):
    return a**b

k = exponential(3,2)
print(k)

def grade(point):
    if point >= 90:
        return "A"
    elif 80 <= point < 90:
        return "B"
    elif 70 <= point < 80:
        return "C"
    elif 60 <= point <70:
        return "D"
    elif point <60:
        return "F"

jenny = grade(88)
print(jenny)