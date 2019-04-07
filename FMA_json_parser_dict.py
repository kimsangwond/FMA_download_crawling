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

genre=input('input genre: ')

def fma_Crawling(html):
	temp_dict = {}
	div_list = html.find_all('div', {'class': 'play-item'})
	artist_list = []
	track_list = []
	album_list = []
	genre_list = []

	for div in div_list :
		global count
		count=0
		count +=1
		print(count)
		artist = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-artist'}).text
		track = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-track'}).text
		album = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-album'}).text
		genre = div.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-genre'}).text
		#artist

		for i in range(1,200) :
			temp_dict[str(i)]={'artist':artist, 'track':track, 'album':album, 'genre':genre}

	return temp_dict

def toJson(fma_dict):

    with open('{}_chart.json'.format(genre), 'w', encoding='utf-8') as file :
        json.dump(fma_dict, file, ensure_ascii=False, indent='\t')

fma_dict={}

req1 = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page=1&per_page=200/'.format(genre))

source1 = req1.text
html2 = BeautifulSoup(source1, 'lxml')
final_page2=html2.select('a[href^="https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page="]'.format(genre))
final_page=final_page2[6].text
final_page=int(final_page)

for page in range(1,final_page):
	req = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page={}&per_page=200'.format(genre, page))
	source = req.text
	html = BeautifulSoup(source, 'lxml')

	#fma_temp = fma_Crawling(html)
	fma_dict = dict(fma_dict, **fma_Crawling(html))

#for item in fma_list :
#	print(item)

#for item in fma_dict:
#	print(item, fma_dict[item]['artist'], fma_dict[item]['track'], fma_dict[item]['album'], fma_dict[item]['genre'])

toJson(fma_dict)