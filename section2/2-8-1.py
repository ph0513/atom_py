from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import re
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



# HTML 가져오기
base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote=rep.quote_plus("사자")
url=base+quote

res=req.urlopen(url)
savePath="d:\\imageDown\\"
try:
    if not(os.path.isdir(savePath)): # isdir 폴더 확인
        os.makedirs(os.path.join(savePath)) # 폴더가 없다면 생성 makedirs 폴더 생성
except OSError as e:
    if e.errno!=errno.EEXIST: # 존재하는 오류 외 나머지
        print("Failed to create directory!!!!!")
        raise # 컴파일 하여 폴더 유무를 확인

soup = BeautifulSoup(res,"html.parser")

li_list=soup.select("div.img_area._item > a.thumb._thumb > img")
#print(li_list)

for i, div in enumerate(li_list,1):
    #print(div) # html 태그(통신값)fmf qkedkdha
    #print(div['src'])
    #print("div = ",div['data-source']) # 실제 이미지 다운
    fullfilename=os.path.join(savePath,savePath+str(i)+'.jpg')
    print(fullfilename)
    req.urlretrieve(div['data-source'],fullfilename) # 이미지는 css 에서 data-source 로 받아옴
    print(i)

print("다운로드 완료")
