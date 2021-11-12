from data_scraper import *
def run_instructure_scraper(link):
    Id="GPWP5OU1Q7GE7ZU"
    response=scraper.run(link,id=Id)
    return response