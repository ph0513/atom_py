import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# urllib / requests json 파일로 encoding RestFul (get(server)가져오기,post입력, put, feche(modify),delete ) httpbin(fake server) payload :

# Response 상태코드 첨부
s=requests.session()
r=s.get("http://httpbin.org/get")
print(r.status_code) # 200
print(r.ok) # 연결 확인
# if ok==True :
#     if status_code==200 :

r=s.get("http://jsonplaceholder.typicode.com/posts/1")
print(r.text)
print(r.json()) # 제이슨 형태로 바꿈
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content)
print(r.raw)
