"""
Scraper for the Tuum website.
"""

from common.util import *
from common.Job import Job


url = "https://tuum.com/careers/"


def scrape() -> list:
    soup = get_soup(url)

    jobs = []
    job_wrappers = soup.find_all('tr', class_='job-listing-title')
    for job in job_wrappers:
        job_title = job.find('p', class_='py-4 xs:py-5').text
        job_link = job['data-href']
        job_location = "Tallinn"
        job_obj = Job(job_title, "Tuum", job_location, job_link, "tuum")
        jobs.append(job_obj)

    return jobs
