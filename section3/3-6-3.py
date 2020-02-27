import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_option=Options()
# firefox_option.log.level="trace" # 로그기록 삭제
firefox_option.add_argument("--headless") # 파이어폭스를 cli(눈에 안보임) 로 바꾼다

driver=webdriver.Firefox(firefox_options=firefox_option,
executable_path='D:/atom_py/section3/webdriver/firefox/geckodriver') # cli 옵션을 준다
# driver=webdriver.Firefox(executable_path='D:/atom_py/section3/webdriver/firefox/geckodriver') # gui
driver.set_window_size(1920,1080)
driver.get('http://google.com')
# time.sleep(5) # 과정을 보여준다 implicitly_wait은 접속대기 이다
driver.save_screenshot("D:/atom_py/section3/webdriver/down/website1(f).png")

driver.get('http://daum.net')
# time.sleep(5)
driver.save_screenshot("D:/atom_py/section3/webdriver/down/website2(f).png")
driver.quit()
#gui(chrome,firefox) cli(phantomjs)
print("스크린샷 완료")
