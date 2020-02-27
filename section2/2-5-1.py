from urllib.parse import urljoin

basicURL="http://test.com/html/a.html"
print(urljoin(basicURL,"b.html"))
print(urljoin(basicURL,"sub/c.html"))
print(urljoin(basicURL,"../index.html"))
print(urljoin(basicURL,"../img/hong.png"))
print(urljoin(basicURL,"../css/hong.css"))
