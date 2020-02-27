import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


s=requests.session()
r=s.get("http://httpbin.org/stream/20")
if r.encoding==None :
# if r.encoding is None :
     r.encoding='utf-8'
#print(r.encoding) # encoding이 안되어 있으면 None 값 반환  utf-8 로만 바뀜
# print(r.status_code)
# print(r.ok)

# print(r.text)

for line in r.iter_lines(decode_unicode=True): # 이걸해야 utf-8 로 바뀐다 #iter_lines(decode_unicode=True) 하나씩 디코딩한다
    print(line)
    b=json.loads(line)
    print(b.keys())# 키값 확인
    for e in b.keys():
        print("key :",e,", values : ",b[e])

# print(r.json())


# print(r.json().keys())
# print(r.json().values())
# print(r.content)
# print(r.raw)
