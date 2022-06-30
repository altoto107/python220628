#Web1.py
#웹크롤링을 위한 선언
from pydoc import pager
from bs4 import BeautifulSoup

page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup, prettify())
#<p>태그 몽땅 검색
#print(soup.find_all("p"))
#첫번째 <p>태그 검색
#print(soup.find("p"))

#조건이 있는 경우 : <p class="outer-text">
#print(soup.find_all("p", calss_="outer-test"))

#ID 속성으로 검색
#print(soup.find_all(id="first"))

#태그 안쪽의 문자열 데이터 
for item in soup.find_all("p"):
    title = item.text
    title = title.replace("\n","")
    title = title.replace("\t ","")
    print(title.strip())
