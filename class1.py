#class1.py

#1) 클래식 형식을 정의 
class Person:
    #초기화 메서드
    def __init__(self):
        self.name="default name"
    #인스턴트 메서드
    def print(self):
        print("My name is {0}".format(self.name) )

#2 인스턴스 생성
p1 = Person()
#3 매서드 호출
p1.print()
    