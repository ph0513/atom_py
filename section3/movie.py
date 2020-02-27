import sys
import io
import requests, json
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 로그인 유저 정보
# LOGIN_INFO={
#     'user_id':'ph0513',
#     'user_pw':'ph0513ph'
# }

# Session 생성, with  구문 안에서 유지
# with requests.Session() as s:
#     # 게시글 가져오기
#     login_req=s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO) # put 도 가능
    # HTML 소스 확인
    # print(login_req.text)
    # HTTP Header 확인
    # print('login_header : ',login_req.headers)
    # Response 정상확인
    # if login_req.status_code == 200 and login_req.ok:
    #     print("로그인 성공")
    # login_req.raise_for_status()
    # print(login_req.status_code)
    # print(login_req.ok)


    # BeautifulSoup 선언 및 확인
with requests.Session() as s:
    r=s.get("https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=37886&type=after&page=1")
    soup=BeautifulSoup(r.content,'html.parser')
    # article=soup.find('div', {'class': 'score_result'})
    article=soup.select_one('div', {'class': 'score_result'})
    # print(article)
    # scores=article.findAll('li')
    scores=article.select('li > div > p > span')
    # print(scores)
    # scores
    # print(scores)
    # review_text = scores.find('')
    # nickname = scores[0].findAll('a')[0].find('span').string
    # score = scores[0].find('em').getText()
    #
    #
    # print(nickname)
    # print(review_text)
    # print(score)

    for i in len(scores):
        if i.string is not None:
            print(i.string)


    # score = scores.('em')
    # print(score)



    # print(soup)
# test_url = "https://movie.naver.com/movie/bi/mi/point.nhn?code=37886"
# resp = requests.get(test_url)
# html = BeautifulSoup(resp.content, 'html.parser')
# html
# score_result = html.find('div', {'class': 'score_result'})
# lis = score_result.findAll('li')
# lis[0]
#body > div > div > div.score_result > ul > li:nth-child(1) > div.score_reple
# body > div > div > div.score_result
# body > div > div

# body > div > div > div.score_result > ul

#     if i.find("a") is None:
#         print(i.string)

    # for i in article:
    #     print(i.text)
