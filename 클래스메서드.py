# 클래스메서드.py
class CoeffVar(object):
    coefficient = 1 
    @classmethod
    def mul(cls, fact):
        return cls.coefficient * fact 

#파생형식을 정의
#정적 메소드는 별도 인스턴스를 만들 필요 없이 활용
class MulFive(CoeffVar):
    coefficient = 5 

x = MulFive.mul(4)
print(x)


