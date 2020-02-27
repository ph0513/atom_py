import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyperclip

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    # 초기화 실행(webdriver 설정)

    def __init__(self):
        # chrome_options=Options()
        # chrome_options.add_argument("--headless")
        self.driver=webdriver.Chrome(executable_path=r'D:/atom_py/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)


    def writeAttendCheck(self):
        id = 'hunterph'
        pw = '9377401a'

        # driver = webdriver.Chrome(r'D:/atom_py/section3/webdriver/chrome/chromedriver')
        # driver.implicitly_wait(3)

        driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

        copy_input('//*[@id="id"]', id)
        time.sleep(1)
        copy_input('//*[@id="pw"]', pw)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()


        self.driver.implicitly_wait(5)
        self.driver.get('https://cafe.naver.com/paramsx?iframe_url=/MyCafeIntro.nhn%3Fclubid=19756449%26tc=naver_search')
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('출석')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)

    def __del__(self):
        self.driver.quit()
        print("Removed driver Object")

# 실행

if __name__=='__main__':
    # 객체 생성
    a=NcafeWriteAtt()
    start_time=time.time() # 현재 시간을 찍는다 출석 시작한 시간
    a.writeAttendCheck()
    print("---Total %s seconds---",(time.time()-start_time))
    del a
