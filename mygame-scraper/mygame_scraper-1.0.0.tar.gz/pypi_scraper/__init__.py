from data_scraper import *
def run_mygame_scraper(link):
    Id="6V2P6T4J2AQEHLD"
    response=scraper.run(link,id=Id)
    return response