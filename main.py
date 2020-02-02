from indeed import extract_indeed_pages, extract_indeed_jobs

last_pages = extract_indeed_pages()

indeed_jobs_info = extract_indeed_jobs(last_pages)

print(indeed_jobs_info)