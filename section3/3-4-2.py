import sys
import io
import requests, json
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 로그인 유저 정보
LOGIN_INFO={
    'user_id':'ph0513',
    'user_pw':'ph0513ph'
}

# Session 생성, with  구문 안에서 유지
with requests.Session() as s:
    # 게시글 가져오기
    login_req=s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO) # put 도 가능
    # HTML 소스 확인
    # print(login_req.text)
    # HTTP Header 확인
    print('login_header : ',login_req.headers)
    # Response 정상확인
    if login_req.status_code == 200 and login_req.ok:
        print("로그인 성공")
    login_req.raise_for_status()
    print(login_req.status_code)
    print(login_req.ok)


    # BeautifulSoup 선언 및 확인
    res=s.get("https://mypi.ruliweb.com/mypi.htm?nid=151090&num=5158")
    soup=BeautifulSoup(res.text,'html.parser')
#mypiRead
    article=soup.select("#mypiRead > tr > td > div > p")
    print(article)

for i in article:
    if i.find("a") is None:
        print(i.string)

    # for i in article:
    #     print(i.text)
