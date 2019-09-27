#list
mylist = [1, 2, 3, 4, 5]
mylist1 = ['a', 'b', 'c']
mylist2 = [1, 'a', [100, 200, 300], 2]

#list 인덱스
print(mylist[1])
print(mylist2[2][1])
#mylist2[3] = 100 
print(mylist2)

#List size
print(len(mylist))
print(len(mylist2))

#append함수
data1 = ["korea", "Japan", "America"]
data1.append("china")
print(data1)

#pop함수
data2 = ['apple', 'banana', 'grape']
#data2.pop()
print(data2)

#sort함수
data3 = ["korean", "english", "science", "art"]
data3.sort()
print(data3)

#list형변환, list함수
data4 = ("hello", "hi", "bye")
d = range(1,10)
data4 = list(data4)
print(data4)
print(type(d))
print(type(list(d)))


#dictionary
mydict = {"korea":82, "Japan":81, "Ameraca":1, "Italy":42}
print(mydict)


#key값으로 접근
print(mydict.keys())
print(mydict['korea'])
#print(mydict[1])

#value값으로 접근
print(mydict.values())
#print(mydict[42]) -> key error, []는 키를 접근.

#items
print(mydict.items())


#tuple, tuple인덱싱
mytuple = (1, 3, 5, 7, 9)
print(mytuple)
print(mytuple[1])

#tuple의 불변 -> error
#mytuple.append(10)
#mytuple[1] = 4

#list와 tuple의 사이즈 비교
import sys

mylist = [1, 3, 5, 7, 9]

print(sys.getsizeof(mylist))
print(sys.getsizeof(mytuple))

#변수 할당
a = 3, 5, 7
print(a)

#list더하기 연산자
h = data1 + mylist
print(h)
