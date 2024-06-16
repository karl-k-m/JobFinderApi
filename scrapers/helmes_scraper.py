"""
A scraper for the Helmes website.
"""

from common.util import *
from common.Job import Job


url = "https://www.helmes.com/career/"


def scrape() -> list:
    soup = get_soup(url)

    jobs = []
    job_list = soup.find_all('div', class_='job-offers__list')
    internal_container = job_list[0]

    for city in internal_container.find_all('div', class_='job-offers__city'):
        city_name = city.find('h4').text
        if "Est" not in city_name:
            continue
        city_jobs = city.find_all('a')
        for job in city_jobs:
            job_title = job.text
            job_link = job['href']
            job_obj = Job(job_title, "Helmes", city_name, job_link, "helmes")
            jobs.append(job_obj)

    return jobs