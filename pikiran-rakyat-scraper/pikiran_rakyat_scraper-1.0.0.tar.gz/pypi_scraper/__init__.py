from data_scraper import *
def run_pikiran_rakyat_scraper(link):
    Id="TC5S3CB7G84OJUC"
    response=scraper.run(link,id=Id)
    return response