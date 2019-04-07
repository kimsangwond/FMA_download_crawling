import requests
import json
from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(10**6)

print('Blues')
print('Classical')
print('Country')
print('Electronic')
print('Experimental')
print('Folk')
print('Hip-Hop')
print('Instrumental')
print('International')
print('Jazz')
print('novelty')
print('Old-Time__Historic')
print('Pop')
print('Rock')
print('Soul-RB')
print('Spoken')

genre=input('input genere: ')

def fma_Crawling(html):
	temp_list = []
	div_list = html.find_all('div', {'class': 'play-item'})

	for div in div_list :

		artist = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-artist'}).text
		track = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-track'}).text
		album = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-album'}).text
		genre = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-genre'}).text
		temp_list.append([artist.strip(), track.strip(), album.strip(), genre.strip()])

	return temp_list

def toJson(fma_list):

    with open('{}_chart.json'.format(genre), 'w', encoding='utf-8') as file :
        json.dump(fma_list, file, ensure_ascii=False, indent='\t')
fma_list=[]

req1 = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page=1&per_page=200/'.format(genre))

source1 = req1.text
html2 = BeautifulSoup(source1, 'lxml')
final_page2=html2.select('a[href^="https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page="]'.format(genre))
final_page=final_page2[6].text
final_page=int(final_page)
print(final_page)

for page in range(1,final_page):
	print(page)
	req = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page={}&per_page=200'.format(genre, page))
	source = req.text
	html = BeautifulSoup(source, 'lxml')
	fma_list += fma_Crawling(html)


#final_page1=html.find_all('div', {'class':'pagination-full'})

for item in fma_list :
	print(item)

toJson(fma_list)