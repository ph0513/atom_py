import sys
import io
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt :
    #초기화 실행(webdriver설정)
    def __init__(self) :
        option = Options()
        # option.add_argument("--headless") #cli
        self.driver =  webdriver.Chrome(executable_path=r'D:/atom_py/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

    def writeAttendCheck(self) :
        self.driver.get('https://nid.naver.com/nidlogin.login')

        pyperclip.copy('hunterph')   #아이디입력
        self.driver.find_element_by_name('id').click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()


        pyperclip.copy('9377401a')   #비밀번호 입력
        self.driver.find_element_by_name('pw').click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()



        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        time.sleep(3)

        self.driver.implicitly_wait(5)
        self.driver.get('http://cafe.naver.com/paramsx?iframe_url=/AttendanceView.nhn%3Fsearch.clubid=19756449%26search.menuid=103')
        self.driver.implicitly_wait(5)
        time.sleep(3)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_xpath('//*[@id="cmtinput"]').send_keys('출석')
        self.driver.find_element_by_xpath('//*[@id="btn-submit-attendance"]').click()
        time.sleep(3)


    def __del__(self) :
        self.driver.quit()
        print("Removed driver Object")

#실행 메인

if __name__ == '__main__' :
    #객체 생성
    a = NcafeWriteAtt()
    start_time = time.time()
    a.writeAttendCheck()
    print("---Total %s seconds " % (time.time()-start_time))
    time.sleep(10)
    del a
