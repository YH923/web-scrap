import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.indeed.com/jobs?q=python&limit=50')
soup = BeautifulSoup(r.text, 'html.parser')

pagination = soup.find("div",{"class":"pagination"});


anchor = pagination.find_all('a')

links=[]
for link in anchor[:-1]:
 #links.append(int(link.find("span").text))
 links.append(int(link.string))

print(links)

  