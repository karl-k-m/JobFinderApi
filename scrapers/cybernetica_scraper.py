"""
Scraper for the Cybernetica website.
"""

from common.util import *
from common.Job import Job

url = "https://cyber.ee/careers/open-positions/"


def scrape() -> list:
    soup = get_soup(url)

    jobs = []
    job_grid = soup.find('section', class_='open-positions-grid')
    job_wrappers = job_grid.find_all('a', class_='link-box')

    for job in job_wrappers:
        job_title = job.find('h2').text
        if "Don't see an opening for your profile" in job_title:
            continue
        job_link = job['href']
        job_location = job.find('p', itemprop='addressLocality').text
        job_obj = Job(job_title, "Cybernetica", job_location, job_link, "cybernetica")
        jobs.append(job_obj)

    return jobs