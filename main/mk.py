
import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bss

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver

# from bs4 import BeautifulSoup as bss


# 모든 https 통신은 필요한 인증서와 호스트명을 기본적으로 체크하게 됨
# 영향 받는 라이브러리는 urllib, urllib2, http, httplib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Boannews Base URL
base_url2 = 'https://www.mk.co.kr/news/economy/latest/'
# base_url2 = base_url + 'media/list.asp?mkind=1'

# print('base_url2>>>', base_url2)




# ='https://www.boannews.com/media/list.asp?mkind=1'
# https://www.boannews.com/media/view.asp?idx=85674


# url = base_url + 'idx=85674'
# url = base_url + 'view.asp?idx='
# url = 'https://www.boannews.com/media/view.asp?idx='





f = urlopen(base_url2)

b = f.read()
soup = bss(b, 'html.parser')
# print(soup)



# divs = soup.find_all('li', {'class' : 'news_node'})
divs = soup.select('li[data-li]')
# divs = soup.find_all('div', {'class' : 'news_ttl'})

# title, url, number 가져오기
print(divs)

file_data = []  

def getMkData():
	num = 0
	for i in divs:
		f = {}
		title = i.find('h3', {'class' : 'news_ttl'})
		title = title.string
	

		# <li class="news_node">
		# <a class="news_item" href="https://www.mk.co.kr/news/economy/10703567">
		# <em class="num c_point">10</em>
		# <h3 class="news_ttl">[단독] 다야니家에 패배했던 韓 236억 추가로 물어줄 판</h3>   
		# </a>
		# </li>


		# date = i.find_all('span')[1]
		# date = date.string
		# date = date.split('|')[1]
		# date = date.replace(' ','',3)
		# date = date.replace('년','-')
		# date = date.replace('월','-')
		# date = date.replace('일','')


		# date = i.find("div", "time_area")
		# date = i.find_all('span')[0]

		# <span>
		# 04.04<br/>
		# 2023
		# </span>
		
		
		# /media/view.asp?idx=85672&page=1&mkind=1&kind=2
		
		# url = i.find_all('a', {'class' : 'news_item'})
		url = i.find('a')['href']
		# print(url)

		# url = base_url + url
		num += 1
		
		# 뉴스 작성 날짜 노출 결정하기
		f['num'] = num
		f['title'] = title
		# f['date'] = date
		f['url'] = url
		
		file_data.append(f)
	return file_data

getMkData()
