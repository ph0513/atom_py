#CSRF(Cross Site Reguest Forgery) 공격을 방어 -> CRRFToken
# 웹 어플리케이션의 취약점을 이용하여 해커가 관리자로 진입후 악의적으로 수정 변조하는 방법
#css
#id='#1 0r 1'
#pw='1 or 1'
import sys
import io
import requests, json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# 요청
url="https://www.wishket.com/accounts/login/"

with requests.Session() as s:
    # URL 요청
    s.get(url)

    # fake_useragent
    ua=UserAgent()
    # print(ua.chrome)
    # print(ua.ie)
    # print(ua.random)
    # login 정보 payload
    LOGIN_INFO={
    'identification': 'ph0513',
    'password': 'ph0513ph',
    'csrfmiddlewaretoken':s.cookies['csrftoken']
    }
    # print('token',s.cookies['csrftoken'])
    # print('headers',s.headers)
    # 요청
    response=s.post(url,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome),'Referer':'https://www.wishket.com/accounts/login/'})
    # html 결과 확인
    # print('response',response.text)
    if response.status_code == 200 and response.ok:

        soup=BeautifulSoup(response.text,'html.parser')
        # project=soup.select("div.sidebar > div > div.partners-history")
        project=soup.select("#wrap > div.page > div.sidebar > div > div.partners-history > div > table > tbody > tr")
        # print(article)
        #wrap > div.page > div.sidebar > div > div.partners-history > div > table > tbody > tr:nth-child(1) > th

    for i in project:
        print(i.text)
