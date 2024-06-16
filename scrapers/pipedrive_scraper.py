"""
Scraper for the Pipedrive website.
"""

from common.util import *
from common.Job import Job


url = "https://www.pipedrive.com/en/jobs/open-positions?location=estonia"


def scrape() -> list:
    soup = get_soup(url)

    jobs = []
    job_wrappers = soup.find_all('div', class_='puco-flex-row puco-flex-row--direction-row puco-flex-row--align-horizontal-xs-between puco-flex-row--align-horizontal-s-between puco-flex-row--align-horizontal-m-between puco-flex-row--align-horizontal-l-between puco-flex-row--align-horizontal-xl-between')
    for job in job_wrappers:
        job_title = job.find('h5', class_='puco-heading').text
        job_location = job.find('p', class_='puco-text puco-text--display-block puco-text--size-s puco-text--weight-normal').text
        job_link = job.find('a')['href']
        job_obj = Job(job_title, "Pipedrive", job_location, job_link, "pipedrive")
        jobs.append(job_obj)

    return jobs