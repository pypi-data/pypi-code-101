from data_scraper import *
def run_nih_scraper(link):
    Id="4WJ781ERVERFPYP"
    response=scraper.run(link,id=Id)
    return response