import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_option=Options()
chrome_option.add_argument("--headless") # 크롬을 cli(눈에 안보임) 로 바꾼다


# executable_path= 크롬은 다음에 r을 붙여야 한다(정규화)
driver=webdriver.Chrome(chrome_options=chrome_option,
                        executable_path=r'D:/atom_py/section3/webdriver/chrome/chromedriver') #cli
# driver=webdriver.Chrome('D:/atom_py/section3/webdriver/chrome/chromedriver') # gui
driver.set_window_size(1920,1080)
driver.get('http://google.com')
# time.sleep(5) # 과정을 보여준다 implicitly_wait은 접속대기 이다
driver.save_screenshot("D:/atom_py/section3/webdriver/down/website1(c).png")



driver.get('http://daum.net')
# time.sleep(5)
driver.save_screenshot("D:/atom_py/section3/webdriver/down/website2(c).png")
driver.quit()
#gui(chrome) cli(phantomjs)
print("스크린샷 완료")
