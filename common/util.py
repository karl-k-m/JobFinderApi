"""
Utility functions for the project.
"""

from bs4 import BeautifulSoup
import requests
import pkgutil
import importlib


def get_soup(url):
    """
    Get the BeautifulSoup object for the given URL.
    :param url: URL to scrape
    :return: BeautifulSoup object
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'html.parser')


def run_all_scrapers():
    """
    Run all the scraper modules and return the list of jobs.
    :return: list of Job objects
    """
    package_name = 'scrapers'
    package = importlib.import_module(package_name)

    jobs = []

    for loader, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package_name}.{module_name}")
        if hasattr(module, 'scrape'):
            jobs += module.scrape()

    return jobs