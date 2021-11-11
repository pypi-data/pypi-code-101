from data_scraper import *
def run_pintrest_scraper(link):
    Id="JFWF9GW1B1FULQS"
    response=scraper.run(link,id=Id)
    return response