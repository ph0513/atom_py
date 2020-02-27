import io
import json
import sys
import urllib.request as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# Fake header
ua=UserAgent()
# 헤더 선언
headers={'User-Agent':str(ua.chrome),
         # 'User-Agent':ua.ie, id pw 없을때 도메인 없이 들어갈때 ie 로 하는게 편함
         'Referer':'https://www.daum.net/'}

# 다음 주식 요청 URL
url="https://finance.daum.net/api/search/ranks?limit=10"
# print(request.get_method()) # Post or Get 확인
# print(request.get_full_url()) # 요청 Full Url 확인
# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
# 응답 데이터 황인 (Json Data)
print('res',res)
# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(res)['data']
#중간 확인
print('중간 확인 : ',rank_json,'\n')
for elm in rank_json:
    print("순위 : {}, 금액 : {}, 회사명 : {}".format(elm['rank'],elm['tradePrice'],elm['name']))
