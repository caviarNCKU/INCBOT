from bs4 import BeautifulSoup
import requests
import sys

def getList(name):
	res = requests.get('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2')
	soup = BeautifulSoup(res.text,'lxml') #analyze with html.parser
	articles = soup.find("table",{"class":"h4"}) #find first table class="h4"

	for row in articles.find_all("tr"):
		data = []
		for col in row.find_all('td'):
			# create dictionary
			col.attrs = {}
			temp = []
			
			#append data in list
			data.append(col.text.strip())
			temp = data[0].split()
			#skip the first row
			if len(data) == 1:
				pass
			else:
				if(temp[0] == name):
					return temp[-1]

def NBAList():
	res = requests.get('http://www.ptt.cc/bbs/NBA/index.html')
	soup = BeautifulSoup(res.text,'lxml')
	articles = soup.find_all('div','r-ent')
	for row in articles:
		meta = row.find('div','title').find('a')
		data = []
		if meta is None:
			pass
		else:
			title = meta.text
			#print(title)
			

def Weather():
	res = requests.get('http://south.cwb.gov.tw/index')
	soup = BeautifulSoup(res.text,'lxml')

	test = soup.find_all('div',{'class':'number'})
	global my_list
	my_list = 'Now tempture:'
	for item2 in test:
		my_list = my_list + item2.text

	my_list = my_list + "  "	
	articles = soup.find_all('div',{'class':'weatherbox'})
	for item in articles:
		my_list = my_list + item.text
	return my_list

NBAList()
