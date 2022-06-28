#class2.py

#1) 클래식 형식을 정의 
class Person:
    #초기화 메서드
    num_person = 0
    def __init__(self):
        self.name="default name"
        Person.num_person += 1
    #인스턴트 메서드
    def print(self):
        print("My name is {0}".format(self.name) )

#2 인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 개수:{0}".format(Person.num_person))

Person.title = "New title"
print(p1.title)
print(p2.title)
print(Person.title)


#인스턴스 추가 
p1.age = 30
print(p1.age)
print(p2.age)
