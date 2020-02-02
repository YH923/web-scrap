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

def extract_indeed_info(html):
  title=html.find("div", {"class" : "title"}).find("a")["title"]

  company = html.find("span", {"class" : "company"})
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = company_anchor.string
  else:
    company = company.string
  company = company.strip()
  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]
  link = f"https://www.indeed.com/jobs?q=python&limit=50&vjk={job_id}"
  return {"title": title, "company" : company, "location" : location, "link" : link}
  
def extract_indeed_jobs(last_page):

  jobs =[]
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get( f"{URL}&start={page * LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')

    lists = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    for list in lists:
      job = extract_indeed_info(list)
      jobs.append(job)  

  return jobs  

     

  


  
    
 
  

