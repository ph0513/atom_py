import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# r = requests.get('https://api.github.com/events')
# r.raise_for_status()# 에러시 장애발생코드 출력 404 403 500
# print(r.text)
# jar=requests.cookies.RequestsCookieJar() # 쿠키접근
# jar.set('name','kim',domain='httpbin.org',path='/cookies')
# jar.set('name','kim') # 생략가능
# r = requests.get('https://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)

# r=requests.get('https://github.com',timeout=3)
# print(r.text)


# Fake Rest : test에 성공하면 메세지로 반환(실제로 처리되지 않음) post put delete
# r=requests.post('https://httpbin.org/post',data={'name':'kim'},cookies=jar)
# print(r.text)

payload1={'key1':'name1','key2':'name2','key3':'name3'} #dict
payload2=(('key1','name1'),('key2','name2'),('key3','name3')) #tuple(보안) # 튜플은 수정 불가
r=requests.post('https://httpbin.org/post',data=payload2)
print(r.text)

payload3={'some':'nice'}
r=requests.post('https://httpbin.org/post',data=json.dumps(payload3))
print(r.text)
