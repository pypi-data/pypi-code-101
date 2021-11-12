from data_scraper import *
def run_huangiu_scraper(link):
    Id="HCSXKL7ZLNHTYHR"
    response=scraper.run(link,id=Id)
    return response