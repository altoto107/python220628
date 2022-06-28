#Function3.py

from re import A, X


x = 2
def func1(a):
    return a+x

#호출
print(func1(1))

#함수 정의
def func2(a):
    X = 5
    return a+X

#함수 호출 
print(func2(1))


#불변 양식, NVRAM 과 유사,  
print("---불변형시---")
a = 1.2
print(id(a))
a =2.3
print(id(a))

#가변 양식 
print("---가변양식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))



#불변형식을 함수 내부에서 읽기+쓰기
g = 1
#전역 변수
def testScope(a):
    global g
    g = 2
#내부 변수에서 2로 변경
    return g+a

#호출 
print(testScope(1))
print("전역 변수 g:", g)


