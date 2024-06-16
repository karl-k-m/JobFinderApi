# JobFinder

![image](https://github.com/karl-k-m/JobFinderApi/assets/74490726/2139f71e-ed00-4420-9ce6-2150faffe6bf)


## About
Looking for jobs is really annoying. This is especially the case because for some god forsaken reason, most Estonian tech companies don't actually list their openings in the common job portals, only on their Careers page. So I made a scraper for it.
This is **NOT** a bot for sending out job applications. It just finds the jobs so you don't have to look through dozens of different careers pages.

I'll add more scrapers for different companies if I feel like it at some point.

## Specs
The API is built with Flask. The Python version used is 3.11. A simple web-UI is provided (index.html). 

The only API endpoint is `/scrape_all`. This will use all the scrapers under the `/scrapers` package and return the data in the following format:
```
{
  "jobs": [
    {
      "company": "Adcash",
      "internalname": "adcash",
      "link": "https://careers.adcash.com/jobs/4561598-devops-intern",
      "location": "Tallinn",
      "title": "DevOps Intern"
    },
    ...
  ]
}
```
The `internalfield` data is actually irrelevant and is there because I cannibalized a bunch of code from a previous iteration of this project. I am, however, too lazy to remove it.

## Usage
To use, simply run `pip install -r requirements.txt` in the project root directory. Then, run app.py with `python3 app.py` (Linux) or `py app.py` (Windows). You can then use the web-UI (index.html).
