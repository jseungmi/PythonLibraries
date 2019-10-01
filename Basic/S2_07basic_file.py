#file객체생성
points = {"korean" : 80, "science" : 90, "math" : 70, "English" : 66}

f = open("jenny_grade.txt", "w")
f.write("jenny\n")
for i in points.items():
    f.write(str(i)+'\n')
    print(i)
f.close()


points_2 = {"korean" : 90, "science" : 80, "math" : 100, "English" : 50}

with open("jenny_grade.txt","a") as f1:
    f1.write("jake\n")
    for j in points_2.items():
        f1.write(str(j)+'\n')
    
