from bs4 import BeautifulSoup
import sys
import io
import re


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp=open("D:/atom_py/section2/food-list.html",encoding="utf-8")

soup=BeautifulSoup(fp,"html.parser")
print(soup)

# 양주 출력
print("1,",soup.select_one("#ac-list > li:nth-of-type(4)").string) # child는 모든 자식이다(손자...)

# print("2,",soup.select("li:nth-of-type(4)")[0].string) # select 는 전부 가져오기 때문에 몇번째 그룹인지 []를 줘야함
print("3,",soup.select("li:nth-of-type(4)")[1].string)
print("4,",soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("5,",soup.select("#ac-list > li.alcohol.high")[0].string)

print()

#삼겹살 출력
# print('1,',soup.select_one("#fd-list>li:nth-of-type(3)").string)
# print('2,',soup.select("li:nth-of-type(3)")[0].string)
# print('3,',soup.select("#fd-list>li[data-lo='ko']")[1].string)
# print('4,',soup.select("#fd-list>li.food.hot")[1].string) # food.hot .은 뛰어쓰기로 인식

param={"data-lo":"cn","class":"alcohol"}
print("6,",soup.find("li",param).string)

print("7,",soup.find(id="ac-list").find("li",param).string)


for ac in soup.find_all("li"):
    if ac['data-lo']=='us':
        print('data-lo==us',ac.string)
        # print(ac.string)

# 삼겹살을 find data-lo":"ko","class":"food hot 이 같이서 실패
# param={"data-lo":"ko","class":"food hot"}
# print(soup.find(id="fd-list").find("li",param).string)



# find_all(필터링=ko)

for ac in soup.find_all("li"):
    if ac['data-lo']=='ko':
        print('data-lo==ko',ac.string)
