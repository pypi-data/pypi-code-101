from data_scraper import *
def run_udemy_scraper(link):
    Id="331XWFKJUGT0KYC"
    response=scraper.run(link,id=Id)
    return response