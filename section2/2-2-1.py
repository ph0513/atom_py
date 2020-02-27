import sys
import io
import urllib.request as dw


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print('하이')



imgurl="https://t1.daumcdn.net/liveboard/Petissue/e0a300be5cc348a299fbae7b6a617d5b.png"
htmlURL="https://www.google.com/"

savePath1="d:/down/test1.jpg"
savePath2="d:/down/index.html"


dw.urlretrieve(imgurl,savePath1)
dw.urlretrieve(htmlURL,savePath2)

print("다운로드 완료!")

# 저장->open('r')->변수방에 할당->파싱->저장
# 다량의 데이터 또는 변수방을 활용하여 파싱할때 사용
