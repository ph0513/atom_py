import sys
import io
from bs4 import BeautifulSoup
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

    def getMemberList(self) :
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
        self.driver.get('https://cafe.naver.com/paramsx?iframe_url=/CafeMemberViewTab.nhn%3FdefaultSearch.clubid=19756449')
        self.driver.implicitly_wait(5)
        # time.sleep(3)
        self.driver.switch_to_frame('cafe_main')
        # print('test',self.driver.page_source)
        self.driver.implicitly_wait(5)
        # html = self.driver.page_source
        # print('test',self.driver.page_source)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        #선택자 추출
        return soup.select('div.ellipsis.m-tcol-c')
        time.sleep(3)


    def printMemberList(self,list):
        f = open('D:/down/memberlist.txt','wt')
        for i in list :
            self.driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/a[i]').click()
            f.write(i.string.strip()+"\n")
            print(i.string.strip())
        f.close()


    def __del__(self) :
        self.driver.quit()
        print("Removed driver Object")






if __name__ == '__main__' :
    #객체 생성
    # self.driver.quit()
    a = NcafeWriteAtt()
    start_time = time.time()
    a.printMemberList(a.getMemberList())
    print("---Total %s seconds " % (time.time()-start_time))
    time.sleep(5)
    del a
