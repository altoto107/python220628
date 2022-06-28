#Function4.py

#기본값이 있는 경우 
from unittest import result


def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자 
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("credu.com","80"))
print(connectURI(port="80",server="credu.com"))

#가변 인자
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result


#호출 
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

