from data_scraper import *
def run_pypi_scraper(link):
    Id="SOY3BJIM9Y3LDN6"
    response=scraper.run(link,id=Id)
    return response