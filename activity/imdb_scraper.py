import os
import requests
import re
from bs4 import BeautifulSoup
import sys
import json

type = sys.getfilesystemencoding()
print(type)
# request the webpage
req = requests.get("https://www.imdb.com/chart/top")
page = req.text

soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())

#get top 250 movie names and years, may take ~30 seconds
movie_names = []
movie_year = [0] * 250

j = 0
for i in range(250):
    content = str(soup.findAll('td', {'class':'titleColumn'})[i])
    name = re.findall ( '>(.*?)</a>', content)
    movie_names.extend(name)

    year = str(soup.findAll('span', {'class':'secondaryInfo'})[i])
    movie_year[i] = int(re.findall(r"\(([0-9_]+)\)", year)[0])

# keep track of the progress

    print('We now have ' + str(j) + ' movies')
    j = j+1


#importing all my keys and tokens from the data file
import json

#importing all my keys and tokens from the data file
with open("activities.json") as f:
    info = json.load(f)

print(info)

info["movie"] = movie_names

with open("activities.json", "w") as out:
    json.dump(info, out, indent=4)


print(movie_names)
