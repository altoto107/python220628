#demoDict.py

from os import device_encoding


print("id: %s, name: %s" % ("kim", "김유신"))

# 형식을 변경
a = set ((1,2,3,))
print(type(a))
print(a)
b = list(a)
print(type(b))
b.append(4)
print(b)


#딕셔너리
color = {"apple":"red","kiwi":"green"}
print(type(color))
print(color)
print(len(color))
color["banana"]="yellow"
print(color)
for item in color.items():
    print(item)

for k,v in color.items():
    print(k, v)


#디바이스 관리 
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device)
device["맥북"]=15
print(device)
device["아이폰"]=6
del device["윈도우"]
print(device)





