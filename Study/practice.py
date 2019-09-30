import os

# file open ex
f = open("/Users/jooyoungson/Documents/GitHub/DevPy/PythonLibraries/Study/hello.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#line4, 경로설정tip : 터미널 창에, pwd를 입력하면 현재 경로가 나옴. 
#line4, 경로설정tip : dir = os.path.dirname(os.path.realpath(__file__))