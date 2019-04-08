from bs4 import BeautifulSoup
import requests


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
	tem_list = []
	track_list = html.find_all('div', {'class': 'play-item'})

	for track in track_list :
		track = track.find('div',{'class':'playtxt'}).find('span',{'class':'ptxt-track'}).text
		track1= str(track)

		tem_list.append([track1.strip()])

	return tem_list


def fma_Download(html):
	temp_list = []
	div_list = html.find_all('div', {'class': 'play-item'})
	
	for div in div_list :
		down1= div.find('span', {'class': 'playicn'}).find("a")
		down2=str(down1)
		down3=down2[27:111]

		temp_list.append([down3])

	return temp_list

def download(url, song_name):
	file_name = url.split('/')[-1]
	name= song_name+".mp3"
	print(name)

	with open(name, "wb") as file:
			response = requests.get(url)
			file.write(response.content)

if __name__ == '__main__':

	fma_download_list=[]
	fma_list=[]

	req1 = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page=1&per_page=200/'.format(genre))

	source1 = req1.text
	html2 = BeautifulSoup(source1, 'lxml')
	
	final_page2=html2.select('a[href^="https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page="]'.format(genre))
	final_page=final_page2[6].text
	final_page=int(final_page)

	final_song2=html2.find('div', {'class': 'pagination-full'}).find_all("b")
	final_song=final_song2[2].text
	final_song=int(final_song)

	for page in range(1,final_page+1):
		req = requests.get('https://freemusicarchive.org/genre/{}/?sort=track_date_published&d=1&page={}&per_page=200'.format(genre, page))
		source = req.text
		html = BeautifulSoup(source, 'lxml')
		fma_download_list += fma_Download(html)
		fma_list += fma_Crawling(html)

	for sang in range(0, final_song):
		url=" ".join(fma_download_list[sang])
		song_name1=fma_list[sang]
		song_name=" ".join(fma_list[sang])
		print(url)
		download(url,song_name)
