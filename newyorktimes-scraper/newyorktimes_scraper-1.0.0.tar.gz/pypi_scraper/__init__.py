from data_scraper import *
def run_newyorktimes_scraper(link):
    Id="9XMUAPOUPIUO770"
    response=scraper.run(link,id=Id)
    return response