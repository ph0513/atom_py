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


#dw.urlretrieve(imgurl,savePath1) # 다이렉트 방식
#dw.urlretrieve(htmlURL,savePath2)

# 1. f=dw.urlopen(imgurl).read()
f2=dw.urlopen(htmlURL).read() # 메모리 적재 방식

# 1. saveFile1=open(savePath1,'wb') #write 바이너리
# 1. saveFile1.write(f)
# 1. saveFile1.close() # 오픈한걸 반드시 닫아야 한다.

with open(savePath2,'wb') as savePath2:
    savePath2.write(f2) # 위드문을 쓰면 클로즈 안써도 된다

print("다운로드 완료!")



imgDown="https://tourimage.interpark.com/BBS/Tour/FckUpload/201703/discovery_20170323_6362582542356180960.jpg"
htmlDown="https://www.naver.com/"


savePath3="d:/down/test2.jpg"
savePath4="d:/down/index2.html"
f3=dw.urlopen(imgDown).read()
with open(savePath3,'wb') as savePath3:
    savePath3.write(f3)
print("대따")
f4=dw.urlopen(htmlDown).read()
with open(savePath4,'wb') as savePath4:
    savePath4.write(f4)
print("대따")
