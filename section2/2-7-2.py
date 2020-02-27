from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="https://finance.naver.com/sise/"
# url="https://finance.naver.com/"
res=req.urlopen(url).read().decode('cp949')
soup=BeautifulSoup(res,"html.parser")
# print(soup)
# print('soup : ',soup.prettify())

 #siselist_tab_0 > tbody > tr:nth-child(3) > td:nth-child(4) > a
top = soup.select("#siselist_tab_0 > tr")
# top = soup.select("#_topItems1 > tr")

# for i,e in enumerate(top,1) : # 위에서 1번부터
#     print(i,",",e.find("a").string," : ",e.find("span").string)

# for e in top:
#     print(e)
# i=1
# for e in top:
#     if e.find("a") is not None: # title 이 tltle 로 코딩되어 있음
#         print(i,e.select_one(".tltle").string)
#         print(i,",",e.find("a").string)
#         i+=1

# print('Top 10 종목명 출력')
# for i,e in enumerate(top) :
#     if e.find("a") is not None:
#         i-=1
#         if i>=9:
#             i=i-3
#         print(i-1,e.select_one(".tltle").string)



# print('Top10 종목명 출력')
# a=0
# for i,e in enumerate(top, 1):
#     if e.find("a")!=None:
#         print(i-a,",", e.select_one(".tltle").string)
#     else:
#         a= a+1



print('Top10 현재가 출력')
i = 1
for e in top :
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string,"=",
                e.select_one("td:nth-of-type(5)").string) # 현재가 출력
        i += 1
