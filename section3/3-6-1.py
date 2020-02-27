import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# D:/atom_py/section3/webdriver/phantomjs

driver=webdriver.PhantomJS('D:/atom_py/section3/webdriver/phantomjs/phantomjs') # 이렇게 하면 알아서 가져옴

driver.implicitly_wait(5) # 트레픽이 걸리면 5초만 있다가 돌아와
driver.get('http://google.com')
driver.save_screenshot("D:/atom_py/section3/webdriver/down/website1.png")

driver.implicitly_wait(5)
driver.get('http://daum.net')
driver.save_screenshot("D:/atom_py/section3/webdriver/down/website2.png")
driver.quit()

print("스크린샷 완료")
