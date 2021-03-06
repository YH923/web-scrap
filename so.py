import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = "https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')

  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")

  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  common = html.find("div", {"class" : "fl1"})
  title = common.find("h2").find("a")["title"]
  company, location = common.find("h3").find_all("span", recursive=False)
  # company_row = company_row[0]
  # location = company_row[1]
  company = company.get_text(strip=True);
  location = location.get_text(strip=True);
  job_id = html["data-jobid"]
  link = f"https://stackoverflow.com/{job_id}/jobs?q=python&sort=i"
  print(link)
  return {"title" : title, "company":company, "location" : location, "link" : link}


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SO: page: {page}")
    result = requests.get(f"{URL}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
   
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
  