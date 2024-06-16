"""
Scraper for the Bitweb website.
"""

from common.util import *
from common.Job import Job

url = "https://bitweb.ee/liitu-meiega/"


def scrape() -> list:
    soup = get_soup(url)

    jobs = []
    job_wrappers = soup.find_all('div', class_='job-offer-wrapper')
    for job in job_wrappers:
        job_title = job.find('h2').text
        if "Ei leidnud seda õiget" in job_title:
            continue

        job_location = "Tartu"
        job_link = "https://bitweb.ee/liitu-meiega"  # TODO: fix finding the link (it's there but bs4 doesn't find it)
        job_obj = Job(job_title, "Bitweb", job_location, job_link, "bitweb")
        jobs.append(job_obj)

    return jobs