class Job:
    """
    Class to represent a job listing.
    """

    def __init__(self, title: str, company: str, location: str, link: str, internalname: str):
        self.title = title
        self.company = company
        self.location = location
        self.link = link
        self.internalname = internalname

    def __str__(self):
        return f"{self.title} at {self.company} in {self.location} - {self.link}"

    def to_dict(self):
        return {
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'link': self.link,
            'internalname': self.internalname
        }