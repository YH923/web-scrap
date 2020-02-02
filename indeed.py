import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, 'html.parser')

  pagination = soup.find("div",{"class":"pagination"})

  anchor = pagination.find_all('a')

  pages=[]
  for link in anchor[:-1]:
   pages.append(int(link.string))
   #links.append(int(link.find("span").text))
  
  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):

  for page in range(last_page):
    result = requests.get( f"{URL}&start={page*0}")

    soup = BeautifulSoup(result.text, 'html.parser')

    lists = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    for list in lists:
      title=list.find("div", "title").find("a")["title"]
      print(title)

  


  
    
 
  

