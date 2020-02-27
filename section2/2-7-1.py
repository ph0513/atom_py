from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url="http://finance.daum.net/"
res=req.urlopen(url).read()


soup=BeautifulSoup(res,"html.parser")
print(soup)
print('soup : ',soup.prettify())


top = soup.select("ul#boxTopSearchs > li")

for i,e in enumerate(top,1) : # 위에서 1번부터
    print(i,",",e.find("a").string," : ",e.find("span").string)
