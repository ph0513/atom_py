import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

payload1={'key1':'name1','key2':'name2'} #dict
payload2=(('key1','name1'),('key2','name2')) #tuple(보안) # 튜플은 수정 불가
payload3={'some':'nice'}
# r=requests.put('http://httpbin.org/put',data=payload1)
# print(r.text) # "User-Agent": "python-requests/2.22.0", 사용한 방법

# r=requests.put('http://jsonplaceholder.typicode.com/posts/1',data=payload1)
# print(r.text)

r=requests.delete('http://jsonplaceholder.typicode.com/posts/1')
print(r.text)
