import sys
import io
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import requests, json

with requests.Session() as s:
    #main-area > div.mem_list_wrap > ul > li:nth-child(1) > div > div.nick > div > table > tbody > tr > td > a > div
    html=s.get('https://cafe.naver.com/paramsx?iframe_url=/CafeMemberViewTab.nhn%3FdefaultSearch.clubid=19756449')

    soup = BeautifulSoup(html,'html.parser')
    # print(soup)
    a=soup.select('div.ellipsis.m-tcol-c')
    print(a)
