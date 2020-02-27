import sys
import io
import urllib.request
from urllib.parse import urlparse


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



url="https://www.youtube.com/"

mem=urllib.request.urlopen(url)
# print(type(mem))
# print("geturl : ",mem.geturl())
# print("status : ",mem.status) # 200(정상) 404없는 페이지 403방화벽(차단) 500(서버에러)
# #if status==403 :
# #    print("5분후에 다시 접속하세요")
# #elif
# print('header : ',mem.getheaders())
# print('info : ',mem.info()) # 마니씀
# print("getcode : ",mem.getcode())
# print("read : ",mem.read(10))


print(urlparse("https://www.youtube.com?test=test").query)
