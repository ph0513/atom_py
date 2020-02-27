import sys
import io
import requests, json
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# session 생성, with 구문 안에서 유지

with requests.Session() as s:
    # 게시글 가져오기
    post_one=s.get('https://bbs.ruliweb.com/market/board/1020/read/37546')
    # print(post_one.text)
    # 예외 발생
    post_one.raise_for_status()
    print(post_one.status_code)
    print(post_one.ok)
    # try:
    #     raise Exception('메롱')
    # # 예외 발생 test print
    # except Exception as e:
    #         print(e)

    # BeautifulSoup 선언 및 확인
    # url='https://bbs.ruliweb.com/market/board/1020/read/37546'
    soup=BeautifulSoup(post_one.text,'html.parser')


    # 문서만 추출및 확인(select)
    #board_read > div > div.board_main > div.board_main_view > div.view_content
    #board_read > div > div.board_main > div.board_main_view > div.view_content > div > p:nth-child(1)
    #board_read > div > div.board_main > div.board_main_view > div.view_content > div > p:nth-child(3)
    article=soup.select("div.view_content > div > p")
    print(article)

    #string 처리 (for)
    for i in article:
        # print(a.string)
        if i.find("a") is None:
            print(i.string)
        # if i.string is not None and i.img == None:
            # print(i.string)
