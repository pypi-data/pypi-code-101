from data_scraper import *
def run_gome_scraper(link):
    Id="DS3NEMP9REWJT0H"
    response=scraper.run(link,id=Id)
    return response