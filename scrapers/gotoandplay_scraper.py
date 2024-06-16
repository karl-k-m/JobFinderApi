"""
Scraper for gotoAndPlay website
"""

from common.util import *
from common.Job import Job


url = "https://play.ee/jobs/"


def scrape() -> list:
    soup = get_soup(url)

    jobs = []
    job_wrappers = soup.find_all('a', class_='card')
    for job in job_wrappers:
        job_link = job['href']
        job_title = job.find('h2', class_='card__title').text
        job_location = "Tartu"
        job_obj = Job(job_title, "gotoAndPlay", job_location, job_link, "gotoandplay")
        jobs.append(job_obj)

    return jobs