#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# In[2]:


from bs4 import BeautifulSoup
import requests
import re
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
imdb = []
for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,            
            "rating": ratings[index]}
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Rating:', item['rating'])


# In[3]:


from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
imdb = []
for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,            
            "rating": ratings[index]}
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Rating:', item['rating'])


# In[27]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')

page

soup = BeautifulSoup(page.content)
soup


president_name = soup.find('div', class_="presidentListing")
name = president_name.text.split('\n')[1]
name


president_name = []

for i in soup.find_all('div', class_="presidentListing"):
    president_name.append(i.text.split('\n')[1])

president_name


terms_of_office = soup.find('div', class_="presidentListing").text
term = terms_of_office.split("Term of Office:")[1].strip()
term = term.split('\n')[0].strip()
term


terms_of_office = []

for i in soup.find_all('div', class_="presidentListing"):
    term = i.text.split("Term of Office:")[1].strip()
    term = term.split('\n')[0].strip()
    terms_of_office.append(term)
terms_of_office


df = pd.DataFrame({'President Name' : president_name, 'Terms of Office': terms_of_office, })
df


# In[5]:


from bs4 import BeautifulSoup
import requests
import re
import numpy as np
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
Team_Names=[]
Team_Matches=[]
Team_Points=[]
Team_Rating=[]

Teams = soup.select('span.u-hide-phablet')
for i in Teams[:10]:
  Team_Names.append(i.text.replace('\n', ''))

Nz_Matches=soup.select('td.rankings-block__banner--matches')
Team_Matches.append(Nz_Matches[0].text.replace('\n',''))
Rest_Matches=soup.select('td.table-body__cell.u-center-text')
for i in Rest_Matches[0:17:2]:
  Team_Matches.append(i.text.replace('\n', ''))
Team_Matches

Nz_Points=soup.select('td.rankings-block__banner--points')
Team_Points.append(Nz_Points[0].text.replace('\n',''))
for i in Rest_Matches[1:18:2]:
  Team_Points.append(i.text.replace('\n', ''))
Team_Points

Nz_Rating=soup.select('td.rankings-block__banner--rating.u-text-right')
Team_Rating.append(Nz_Rating[0].text.replace('\n',''))
Team_Rating[0]=Team_Rating[0].replace(' ','')
Rating=soup.select('td.table-body__cell.u-text-right.rating')
for i in Rating[:9]:
  Team_Rating.append(i.text.replace('\n', ''))
Team_Rating

import pandas as pd
ICC_Mens = pd.DataFrame()
#ICC_Mens.index = np.arange(1, len(ICC_Mens))
#ICC_Mens.index = ICC_Mens.index + 1
#ICC_Mens.shift()[1:]
#ICC_Mens.index = np.arange(1, len(ICC_Mens)+1)
ICC_Mens['Team']=Team_Names
ICC_Mens['Matches']=Team_Matches
ICC_Mens['Points']=Team_Points
ICC_Mens['Rating']=Team_Rating
ICC_Mens.index = ICC_Mens.index + 1
ICC_Mens


# In[6]:


from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
Batsman_Names=[]
Batsman_Team=[]
Batsman_Rating=[]
Batsman = soup.select('div.rankings-block__banner--name')
Batsman_Names.append(Batsman[0].text)
rest_Batsman=soup.select('td.table-body__cell.name')
for i in rest_Batsman[:9]:
  Batsman_Names.append(i.text.replace('\n', ''))

Country=soup.select('div.rankings-block__banner--nationality')
temp=[]
temp.append(Country[0].text.replace('\n',''))
temp[0]=temp[0].replace(' ','')
temp_str=""
temp_alphabet=""
temp_number=""
temp_str=str(temp)
temp_alphabet=temp_str[slice(2,5)]
Batsman_Team.append(temp_alphabet)
temp_number=temp_str[slice(5,8)]
Batsman_Rating.append(temp_number)

Rest_Country=soup.select('td.table-body__cell.nationality-logo')
for i in Rest_Country[:9]:
  Batsman_Team.append(i.text.replace('\n', ''))


Rest_Rating=soup.select('td.table-body__cell.u-text-right.rating')
for i in Rest_Rating[:9]:
  Batsman_Rating.append(i.text.replace('\n', ''))

import pandas as pd
ICC_Mens_Batsman = pd.DataFrame({})
ICC_Mens_Batsman['Player']=Batsman_Names
ICC_Mens_Batsman['Team']=Batsman_Team
ICC_Mens_Batsman['Rating']=Batsman_Rating
ICC_Mens_Batsman.index += 1
ICC_Mens_Batsman


# In[7]:


from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
Bowler_Names=[]
Bowler_Team=[]
Bowler_Rating=[]
Bowler = soup.select('div.rankings-block__banner--name')
Bowler_Names.append(Bowler[1].text)
rest_Bowler=soup.select('td.table-body__cell.name')
for i in rest_Bowler[9:18]:
  Bowler_Names.append(i.text.replace('\n', ''))
Country=soup.select('div.rankings-block__banner--nationality')
temp=[]
temp.append(Country[1].text.replace('\n',''))
temp[0]=temp[0].replace(' ','')
temp_str=""
temp_alphabet=""
temp_number=""
temp_str=str(temp)
temp_str
temp_alphabet=temp_str[slice(2,4)]
Bowler_Team.append(temp_alphabet)
temp_number=temp_str[slice(4,7)]
Bowler_Rating.append(temp_number)

Rest_Country=soup.select('td.table-body__cell.nationality-logo')
for i in Rest_Country[9:18]:
  Bowler_Team.append(i.text.replace('\n', ''))

Rest_Rating=soup.select('td.table-body__cell.u-text-right.rating')
for i in Rest_Rating[9:18]:
  Bowler_Rating.append(i.text.replace('\n', ''))
Bowler_Rating

import pandas as pd
ICC_Mens_Bowler = pd.DataFrame({})
ICC_Mens_Bowler['Player']=Bowler_Names
ICC_Mens_Bowler['Team']=Bowler_Team
ICC_Mens_Bowler['Rating']=Bowler_Rating
ICC_Mens_Bowler.index += 1
ICC_Mens_Bowler


# In[8]:


from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
Team_Names=[]
Team_Matches=[]
Team_Points=[]
Team_Rating=[]


Teams = soup.select('span.u-hide-phablet')
for i in Teams[:10]:
  Team_Names.append(i.text.replace('\n', ''))

Aus_Matches=soup.select('td.rankings-block__banner--matches')
Team_Matches.append(Aus_Matches[0].text.replace('\n',''))
Rest_Matches=soup.select('td.table-body__cell.u-center-text')
for i in Rest_Matches[0:17:2]:
  Team_Matches.append(i.text.replace('\n', ''))
Team_Matches

Aus_Points=soup.select('td.rankings-block__banner--points')
Team_Points.append(Aus_Points[0].text.replace('\n',''))
for i in Rest_Matches[1:18:2]:
  Team_Points.append(i.text.replace('\n', ''))
Team_Points

Aus_Rating=soup.select('td.rankings-block__banner--rating.u-text-right')
Team_Rating.append(Aus_Rating[0].text.replace('\n',''))
Team_Rating[0]=Team_Rating[0].replace(' ','')
Rating=soup.select('td.table-body__cell.u-text-right.rating')
for i in Rating[:9]:
  Team_Rating.append(i.text.replace('\n', ''))
Team_Rating

import pandas as pd
ICC_Womens = pd.DataFrame({})
ICC_Womens['Team']=Team_Names
ICC_Womens['Matches']=Team_Matches
ICC_Womens['Points']=Team_Points
ICC_Womens['Rating']=Team_Rating
ICC_Womens.index += 1
ICC_Womens


# In[9]:


from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
Batsman_Names=[]
Batsman_Team=[]
Batsman_Rating=[]
Batsman = soup.select('div.rankings-block__banner--name')
Batsman_Names.append(Batsman[0].text)
Batsman_Names
rest_Batsman=soup.select('td.table-body__cell.name')
for i in rest_Batsman[:9]:
  Batsman_Names.append(i.text.replace('\n', ''))

Country=soup.select('div.rankings-block__banner--nationality')
temp=[]
temp.append(Country[0].text.replace('\n',''))
temp[0]=temp[0].replace(' ','')
temp_str=""
temp_alphabet=""
temp_number=""
temp_str=str(temp)
temp_alphabet=temp_str[slice(2,5)]
Batsman_Team.append(temp_alphabet)
temp_number=temp_str[slice(5,8)]
Batsman_Rating.append(temp_number)

Rest_Country=soup.select('td.table-body__cell.nationality-logo')
for i in Rest_Country[:9]:
  Batsman_Team.append(i.text.replace('\n', ''))


Rest_Rating=soup.select('td.table-body__cell.u-text-right.rating')
for i in Rest_Rating[:9]:
  Batsman_Rating.append(i.text.replace('\n', ''))

import pandas as pd
ICC_Womens_Batsman = pd.DataFrame({})
ICC_Womens_Batsman['Player']=Batsman_Names
ICC_Womens_Batsman['Team']=Batsman_Team
ICC_Womens_Batsman['Rating']=Batsman_Rating
ICC_Womens_Batsman.index += 1
ICC_Womens_Batsman


# In[10]:


from bs4 import BeautifulSoup
import requests
import re
url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
Player_Names=[]
Player_Team=[]
Player_Rating=[]
Player = soup.select('div.rankings-block__banner--name')
Player_Names.append(Player[2].text)
rest_Player=soup.select('td.table-body__cell.name')
for i in rest_Player[18:27]:
  Player_Names.append(i.text.replace('\n', ''))

Country=soup.select('div.rankings-block__banner--nationality')
temp=[]
temp.append(Country[2].text.replace('\n',''))
temp[0]=temp[0].replace(' ','')
temp_str=""
temp_alphabet=""
temp_number=""
temp_str=str(temp)

temp_alphabet=temp_str[slice(2,4)]
Player_Team.append(temp_alphabet)
temp_number=temp_str[slice(4,7)]
Player_Rating.append(temp_number)

Rest_Country=soup.select('td.table-body__cell.nationality-logo')
for i in Rest_Country[18:27]:
  Player_Team.append(i.text.replace('\n', ''))

Rest_Rating=soup.select('td.table-body__cell.u-text-right.rating')
for i in Rest_Rating[18:27]:
  Player_Rating.append(i.text.replace('\n', ''))

import pandas as pd
ICC_Womens_AllRounder = pd.DataFrame({})
ICC_Womens_AllRounder['Player']=Player_Names
ICC_Womens_AllRounder['Team']=Player_Team
ICC_Womens_AllRounder['Rating']=Player_Rating
ICC_Womens_AllRounder.index += 1
ICC_Womens_AllRounder


# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cnbc.com/world/?region=world"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

headlines = []
times = []
links = []

for item in soup.find_all('div', class_='Card-titleContainer'):
    headline = item.find('a').get_text().strip()
    headlines.append(headline)
    
    try:
        time = item.find('time').get_text().strip()
    except AttributeError:
        time = float('NaN')
    times.append(time)
    
    link = item.find('a').get('href')
    links.append(link)

df = pd.DataFrame({'Headline': headlines, 'Time': times, 'News Link': links})
print(df.head())


# In[25]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page

soup = BeautifulSoup(page.content)
soup

paper_title = []

for i in soup.find_all('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)

paper_title

authors = []

for i in soup.find_all('span', class_="sc-1w3fpd7-0 dnCnAO"):
    authors.append(i.text)
    
authors

published_date = []
for i in  soup.find_all('span', class_= "sc-1thf9ly-2 dvggWt"):
    published_date.append(i.text)
    
published_date

urls = []
for i in soup.find_all('a', class_="sc-5smygv-0 fIXTHm"):
    url = i.get('href')
    if url:
        urls.append(url)
        
urls

df = pd.DataFrame({'Paper Title' : paper_title, 'Authors': authors, 'Published Data' : published_date, 'URLS': urls })
df


# In[26]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.dineout.co.in/delhi-restaurants')

page

soup = BeautifulSoup(page.content)
soup

restaurant_name = soup.find('a', class_="restnt-name ellipsis")
restaurant_name
restaurant_name.text


restaurant_name = []

for i in soup.find_all('a', class_="restnt-name ellipsis"):
    restaurant_name.append(i.text)

restaurant_name

cuisine = soup.find('span', class_="double-line-ellipsis")
cuisine.text.split('|')[1]

cuisine = []

for i in soup.find_all('span', class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
    
cuisine

loc = soup.find('div', class_="restnt-loc ellipsis")
loc.text

loc = []

for i in soup.find_all('div', class_="restnt-loc ellipsis"):
    loc.append(i.text)
    
loc


rating = soup.find('div', class_= "restnt-rating rating-4")
rating.text


rating=[]
for i in soup.find_all('div', class_= "restnt-rating rating-4"):
    rating.append(i.text)
    
rating

images = soup.find("img", class_="no-img")
image_src = images.get('data-src')

images = []
for i in soup.find_all("img", class_="no-img"):
    images.append(i.get('data-src'))
images


df = pd.DataFrame({'Restaurant Name' : restaurant_name, 'Cuisine': cuisine, 'Location' : loc, 'Rating': rating, 'Images_url' : images })
df


# In[ ]:




