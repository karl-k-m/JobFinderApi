"""
Scraper for the Playtech website.
"""

from common.util import *
from common.Job import Job


url = "https://www.playtechpeople.com/jobs-our/?activeLocation=Estonia"


def scrape() -> list:
    soup = get_soup(url)
    jobs = []
    job_items = soup.find_all('a', class_='job-item')
    for job in job_items:
        job_title = job.find('h6').text
        job_link = job['href']
        job_location = job.find('p', class_='location-link').text

        if "Estonia" not in job_location:
            continue

        job_obj = Job(job_title, "Playtech", job_location, job_link, "playtech")
        jobs.append(job_obj)

    return jobs