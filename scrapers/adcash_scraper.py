"""
Scraper for the Adcash website.
"""

from common.util import *
from common.Job import Job


url = "https://careers.adcash.com/jobs/"


def scrape() -> list:
    soup = get_soup(url)

    jobs = []
    job_wrappers = soup.find_all('li', class_='z-career-job-card-image')
    for job in job_wrappers:
        job_link = job.find('a', class_='block')['href']
        job_title = job.find('span', class_='text-block-base-link').text
        info_div = job.find('div', class_='mt-1 text-md')
        job_location = info_div.find_all('span')[2].text
        if "Tallinn" not in job_location and "Tartu" not in job_location:
            continue
        job_obj = Job(job_title, "Adcash", job_location, job_link, "adcash")
        jobs.append(job_obj)

    return jobs