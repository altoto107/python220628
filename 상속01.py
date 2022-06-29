#부모 클래스 정의
class Person:
    #초기화 메서드 (생성자)
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    #인스턴스 메서드
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 정의 ()person이 없으면 object에서 받는것 person이 있으니 복사하여 사용
class Student(Person):
    #상속받은 초기화 메서들 재정의
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모클래스의 초기화 메서드를 명시적 호출 
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받은 메서드를 제정의 (덮어쓰기, OVerride)
    def printinfo(self):
          print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
          print("Info(subject:{0}, studentID: {1})".format(
            self.subject, self.studentID))
#인스턴스(복사본) 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "191122")
p.printInfo()
s.printinfo()


#오브젝트 클래스에 정의되어 있는 attribute, 딕셔너리
#print(p.__dict__)
#print(s.__dict__)

