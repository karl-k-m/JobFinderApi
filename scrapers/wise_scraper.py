"""
Scraper for the Wise website.
"""

from common.util import *
from common.Job import Job


# Estonian url, change if you want to scrape from another country
url = "https://wise.jobs/jobs?options=300&page=1"


def scrape() -> list:
    soup = get_soup(url)
    jobs = []
    job_wrappers = soup.find_all('div', class_="attrax-vacancy-tile")

    for job in job_wrappers:
        job_link = "https://wise.jobs" + job.find('a')['href']
        job_title = job.find('a').text.strip()
        job_location = job.find_all('p', class_='attrax-vacancy-tile__item-value')[1].text.strip()
        job_obj = Job(job_title, "Wise", job_location, job_link, "wise")
        jobs.append(job_obj)

    return jobs