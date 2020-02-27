from bs4 import BeautifulSoup
import sys
import io
import re


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html="""
<html><body>
    <ul>
        <li id="naver"><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup=BeautifulSoup(html,'html.parser')
# naver=soup.find(id="naver").string
naver=soup.find(id="naver") # select_one과 동일하게 바로 string 처리 가능
print('naver : '+naver.string)

li=soup.find_all(href=re.compile(r"^https://"))
print('li : ',li)
# for li0 in li:
#     print('li : ',li0.string)
for e in li:
    print(e.attrs['href'])
print('')
li2=soup.find_all(href=re.compile(r"da"))
print('li2 : ',li2)
