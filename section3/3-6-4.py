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



driver=webdriver.Firefox(executable_path='D:/atom_py/section3/webdriver/firefox/geckodriver')
# driver.set_window_size(1280,720)
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www.wishket.com/accounts/login/')
time.sleep(5)
driver.implicitly_wait(3)
driver.find_element_by_name('identification').send_keys('ph0513')
driver.implicitly_wait(3)
driver.find_element_by_name('password').send_keys('ph0513ph')
driver.implicitly_wait(3)
# 로그인
driver.find_element_by_xpath('//*[@id="submit"]').click()
