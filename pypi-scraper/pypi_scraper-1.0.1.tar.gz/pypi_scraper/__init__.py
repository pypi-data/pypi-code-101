from data_scraper import *
def run_pypi_scraper(link):
    Id="415M0JL1U5IPII8"
    response=scraper.run(link,id=Id)
    return response