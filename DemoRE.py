#DemoRE.py

import re
result = re.search("[0-9]*th"," 35th")
#매칭 오브젝트가 리턴
print(result)
print(result.group())

#블럭 주석 처리 : ctrl + /
# result = re.match("[0-9]*th"," 35th")
# print(result)
# print(result.group())

print(bool(re.search("apple", "this is apple")))
#search가 일반적인 검색
print(bool(re.match("apple", "this is apple")))
#match는 앞에만 보고 검색 끝 
