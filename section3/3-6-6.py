import io
import json
import sys
import requests
import urllib.request as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_option=Options()
firefox_option.add_argument("--headless")


driver=webdriver.Firefox(firefox_options=firefox_option,executable_path='D:/atom_py/section3/webdriver/firefox/geckodriver')
# driver.set_window_size(1280,720)
driver.maximize_window()
# driver.implicitly_wait(2)
driver.get('http://www.encar.com/index.do')
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="indexSch1"]/div[1]/a/span').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="stepManufact"]/dl/dd[4]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="stepModel"]/dl[2]/dd[34]/a').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[5]/span[4]/a').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[3]/div[3]/table/tbody/tr[4]/td[1]/div/a/span/span').click()
# driver.switch_to.window(driver.window_handles[0])
# driver.close()
time.sleep(1)
n=find_element_by_css_selector('h1.prod_name > span:nth-child(1)')
print(ㅇ)
# print()
