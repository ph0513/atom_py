from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# """ html 문법
html="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""
soup=BeautifulSoup(html,'html.parser') # html을 parser 해주겠다 하나의 구조, 클래스화

print('soup(type) : ',type(soup))
links=soup.find_all("a")
print('links(type) : ',type(links))
print('links : ',links)

a=soup.find_all("a",string="daum")
print('a : ',a)

b=soup.find("a") # 이건 스트링인듯
print('b : ',b)

c=a=soup.find_all("a",string=["naver","google"])
print('c : ',c)
print('c(type) : ',type(c))

d=soup.find_all("a",limit=2) # limit=0 은 한계가 없다 다가져옴
print('d : ',d)


for a in links:
    # print('a =>',a)
    href=a.attrs['href'] #딕셔너리로 반환 [?]="?" 다  href = "http://www.naver.com"
    text=a.string # <a></a> 태그 안에 있는것
    print(text,">",href)
