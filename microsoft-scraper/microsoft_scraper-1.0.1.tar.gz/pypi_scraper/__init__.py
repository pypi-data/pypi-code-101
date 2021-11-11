from data_scraper import *
def run_microsoft_scraper(link):
    Id="OISJKU23N5ELTFX"
    response=scraper.run(link,id=Id)
    return response