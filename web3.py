# web2.py
#웹크롤링을 위한 선언
from cgitb import text
from turtle import tilt, title
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request
#파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")

#페이징 처리를 하는 경우 , 정수를 문자로 바꾸는 str
for i in range (1,6):
	url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" +str(i)
	print(url)
	data = urllib.request.urlopen(url)
	#검색이 용이한 객체 
	soup = BeautifulSoup(data, "html.parser")
	cartoons = soup.find_all("td", class_="title")
	
	for item in cartoons:
		title = item.find("a").text
		print(title.strip())
        f.write 
        
        

print("---웹 크롤링 종료---")

