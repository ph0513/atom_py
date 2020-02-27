from bs4 import BeautifulSoup
import sys
import io
import re


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp=open("D:/atom_py/section2/cars.html",encoding="utf-8")

soup=BeautifulSoup(fp,"html.parser")

# print(soup)

def car_func(selector):
    print("car_func : ",soup.select_one(selector).string)


car_lambda=lambda q:print("car_func : ",soup.select_one(q).string) # q는 selector다



car_func("#gr")
car_func("li#gr")
car_func("li[id='gr']")
car_func("ul>li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")

print()

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("li[id='gr']")
car_lambda("ul>li#gr")
car_lambda("#cars #gr")
car_lambda("#cars > #gr")




print("select : ",soup.select("li")[3].string)
print("find_all : ",soup.find_all("li")[3].string)
