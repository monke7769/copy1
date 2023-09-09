import sys
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
sys.stdout = open('data.csv','w')

ureq = urlopen('https://www.billboard.com/charts/hot-100/')
html_content = ureq.read()
ureq.close()

soup = BeautifulSoup(html_content, 'html.parser')
s = soup.find('div', class_='chart-results-list')
songnames = s.find_all('h3', id='title-of-a-story')

songs = [] # ***
for i in range(2,400,4):
    name = songnames[i].get_text()
    songs.append(name.strip())
    
spans = s.find_all('span', class_=re.compile('c-label'))
spanlist = []
for i in range(0,len(spans)):
    bald = spans[i].get_text()
    spanlist.append(bald.strip())
spanlist = [i for i in spanlist if i != 'NEW']
# ['100', 'Peso Pluma', '87', '63', '9', '87', '63', '9']
# [pos, artist, lastwk, peakpos, wksonchart, lastwk, peakpos, wksonchart]

artists = [spanlist[i] for i in range(1,794,8)] # ***
lastwk = [spanlist[i] for i in range(2,795,8)] # ***
peakpos = [spanlist[i] for i in range(3,796,8)] # ***
wksonchart = [spanlist[i] for i in range(4,798,8)] # ***

for i in range(100):
    print(str(i+1)+','+songs[i]+','+artists[i]+','+lastwk[i]+','+peakpos[i]+','+wksonchart[i])
