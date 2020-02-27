from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url="https://finance.naver.com/sise/"
res=req.urlopen(url).read().decode('cp949')
soup=BeautifulSoup(res,"html.parser")



rank=soup.select("ul#popularItemList > li")
top10 = soup.select("#popularItemList > li > a")


print("네이버 주식 인기검색 종목 10위")
for i,e in enumerate(rank) :
    print("순위 : {0}, 이름 : {1}".format(i+1   ,e.find("a").string))
    # print('순위 :',i,",","이름 :",e.find("a").string)

for i,e in enumerate(top10, 1):
    print("순위 : {}, 이름 : {}".format(i,e.string))


#contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td:nth-child(2) > a

print("오잉")

url0="https://finance.naver.com/sise/lastsearch2.nhn"
res0=req.urlopen(url0).read()
soup0=BeautifulSoup(res0,"html.parser")

top = soup0.select("div.box_type_l > .table")
print(top)

i = 1
for e in top :
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i += 1



print()
url1="https://www.daum.net/"
res1=req.urlopen(url1).read()
soup1=BeautifulSoup(res1,"html.parser")

main1 = soup1.select("div.realtime_part > .list_hotissue.issue_row > li > div >div[aria-hidden='true']>span.txt_issue a")
print(main1)

for e in main1:
    print(e.string)
    print(e['href'])

for i,e in enumerate(main1,1):
    print(i,':',e.string)
    # print(e['href'])
