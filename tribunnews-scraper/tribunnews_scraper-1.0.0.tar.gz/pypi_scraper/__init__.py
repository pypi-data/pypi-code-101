from data_scraper import *
def run_tribunnews_scraper(link):
    Id="87KS297BWOV3PJX"
    response=scraper.run(link,id=Id)
    return response