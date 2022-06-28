#Function3.py

from re import X


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
