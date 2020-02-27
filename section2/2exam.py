import sys
import io
import urllib.request
from urllib.parse import urlparse


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



imgDown="https://ssl.pstatic.net/tveta/libs/1260/1260649/19aabf7c9a09e0d9ed84_20200211140438611.jpg"
videoDown="https://tvetamovie.pstatic.net/libs/1260/1260649/24e0cefb7bd741f2d0ec_20200211143216244.mp4-pBASE-v0-f98576-20200211143324330.mp4"


savePath1="d:/down/test3.jpg"
savePath2="d:/down/video.mp4"
f1=urllib.request.urlopen(imgDown).read()
with open(savePath1,'wb') as savePath1:
    savePath1.write(f1)
print("대따")
# f2=urllib.request.urlopen(videoDown).read()
# with open(savePath2,'wb') as savePath2:
#     savePath2.write(f2)
# print("대따")



API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
values={'ctxCd':'1001'}

print('before',values)
params=urllib.parse.urlencode(values)
print('after',params) # 가공처리
# 요청 URL 생성
url=API+"?"+params
print("요청 url = ",url)
# 읽기
data=urllib.request.urlopen(url).read()
text=data.decode("utf-8")
print(text)
