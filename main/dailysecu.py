

import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bss



# 모든 https 통신은 필요한 인증서와 호스트명을 기본적으로 체크하게 됨
# 영향 받는 라이브러리는 urllib, urllib2, http, httplib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



# DailySecu Base URL
url = 'https://www.dailysecu.com/news/articleList.html?sc_section_code=S1N6&view_type=sm'

# print('soup>>>>', url)
# url open 
f = urlopen(url)


# page read
b = f.read()

soup = bss(b, 'html.parser')

divs = soup.find_all('div',{'class': 'list-block'})
# print('divs>>>', divs)




file_data = []
def getDailyData():
	num = 0
	for i in divs:
		f = {}
		title = i.find('div', {'class' : 'list-titles'})
		title = title.string

		url = i.find('a')['href']
		# url = base_url + url

		# ex) <span class="list-dated">이슈 | 길민권  기자 | 2019.08.12 12:02</span>
		date = i.find_all('div', {'class': 'list-dated'})[0]
		date = date.string
		date = date.string.partition('|')[2]
		date = date.partition('|')[2]

		# # ex) 2019.08.12 12:02
		# date = date.split(' ')[1]

		num += 1

		f['num'] = num 
		f['date'] = date
		f['title'] = title
		f['url'] = url

		file_data.append(f)
		# print('file_data>>>', file_data)
	
	return file_data

			


getDailyData()





